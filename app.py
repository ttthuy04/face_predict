# app.py
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify, send_file
import cv2
import os
from datetime import datetime
import csv
from app.face_recognizer import load_encodings, recognize_face
from app.utils import get_attendance_data, get_attendance_stats

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Tạo thư mục cần thiết
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('attendance', exist_ok=True)
os.makedirs('encodings', exist_ok=True)

# Camera (sẽ được khởi tạo khi cần)
camera = None

# Load encodings
KNOWN_ENCODINGS = []
KNOWN_NAMES = []

try:
    KNOWN_ENCODINGS, KNOWN_NAMES = load_encodings()
    print(f"Loaded {len(KNOWN_NAMES)} known faces")
except Exception as e:
    print(f"Warning: Could not load encodings: {e}")
    print("Please run train.py first to train the model")

# Attendance folder
ATTENDANCE_DIR = "attendance"
os.makedirs(ATTENDANCE_DIR, exist_ok=True)

def get_camera():
    global camera
    if camera is None:
        # Sử dụng CAP_DSHOW trên Windows để giảm độ trễ
        try:
            camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        except Exception:
            camera = cv2.VideoCapture(0)
        # Thiết lập kích thước khung hình để nhẹ hơn
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return camera

def generate_frames():
    global camera
    camera = get_camera()
    recognized_today = set()  # Để tránh điểm danh nhiều lần
    frame_index = 0
    process_every_n = 2  # xử lý mỗi N khung hình để đỡ giật
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            results = []
            if KNOWN_ENCODINGS and KNOWN_NAMES:
                # Chỉ chạy nhận diện mỗi N khung hình để mượt hơn
                if frame_index % process_every_n == 0:
                    # Giảm kích thước khung để xử lý nhanh hơn
                    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                    # Nhận diện trên khung nhỏ, sau đó scale tọa độ về khung gốc
                    results = recognize_face(small_frame, KNOWN_ENCODINGS, KNOWN_NAMES)
                    scaled_results = []
                    for (top, right, bottom, left), name in results:
                        scaled_results.append(((int(top*2), int(right*2), int(bottom*2), int(left*2)), name))
                    results = scaled_results

                # Vẽ kết quả và điểm danh
                for (top, right, bottom, left), name in results:
                    color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, name, (left, top - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

                    # Auto mark attendance (chỉ 1 lần mỗi ngày cho mỗi người)
                    if name != "Unknown":
                        today = datetime.now().strftime("%Y-%m-%d")
                        key = f"{name}_{today}"
                        if key not in recognized_today:
                            mark_attendance(name, today)
                            recognized_today.add(key)
            else:
                # Hiển thị thông báo nếu chưa train
                cv2.putText(frame, "No trained faces. Please run train.py", 
                          (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            frame_index += 1
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def mark_attendance(name, date):
    if name == "Unknown":
        return
    filename = f"{ATTENDANCE_DIR}/attendance_{date}.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Time"])
        writer.writerow([name, datetime.now().strftime("%H:%M:%S")])

@app.route('/')
def index():
    stats = get_attendance_stats()
    return render_template('index.html', stats=stats)

@app.route('/realtime')
def realtime():
    return render_template('realtime.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        student_name = request.form.get('student_name', '').strip()
        
        if file and student_name:
            # Tạo thư mục cho student
            student_dir = os.path.join('dataset', student_name)
            os.makedirs(student_dir, exist_ok=True)
            
            # Lưu file
            filename = file.filename
            filepath = os.path.join(student_dir, filename)
            file.save(filepath)
            
            return jsonify({'success': True, 'message': f'Uploaded {filename} for {student_name}'})
        else:
            return jsonify({'success': False, 'message': 'Please provide both file and student name'})
    
    return render_template('upload.html')

@app.route('/attendance')
def attendance():
    date = request.args.get('date', datetime.now().strftime("%Y-%m-%d"))
    attendance_data = get_attendance_data(date)
    return render_template('attendance.html', attendance_data=attendance_data, date=date)

@app.route('/api/attendance')
def api_attendance():
    date = request.args.get('date', datetime.now().strftime("%Y-%m-%d"))
    attendance_data = get_attendance_data(date)
    return jsonify(attendance_data)

@app.route('/api/stats')
def api_stats():
    stats = get_attendance_stats()
    return jsonify(stats)

@app.route('/train', methods=['POST'])
def train_model():
    try:
        from train import train
        train()
        # Reload encodings
        global KNOWN_ENCODINGS, KNOWN_NAMES
        KNOWN_ENCODINGS, KNOWN_NAMES = load_encodings()
        return jsonify({'success': True, 'message': 'Training completed successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.teardown_appcontext
def close_camera(error):
    global camera
    if camera is not None:
        camera.release()
        camera = None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)