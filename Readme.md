# 🎯 Hệ Thống Điểm Danh Khuôn Mặt (Face Recognition Attendance System)

Hệ thống nhận diện khuôn mặt và điểm danh tự động sử dụng Flask và face-recognition library.

## 📋 Mục Lục

- [Tính Năng](#tính-năng)
- [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
- [Cài Đặt](#cài-đặt)
- [Cấu Hình](#cấu-hình)
- [Cách Sử Dụng](#cách-sử-dụng)
- [Chạy Ứng Dụng](#chạy-ứng-dụng)
- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [Troubleshooting](#troubleshooting)

## ✨ Tính Năng

- ✅ Nhận diện khuôn mặt thời gian thực từ webcam
- ✅ Điểm danh tự động khi nhận diện được khuôn mặt
- ✅ Upload và quản lý ảnh học sinh
- ✅ Train model từ ảnh đã upload
- ✅ Xem báo cáo điểm danh theo ngày
- ✅ Xuất dữ liệu điểm danh ra CSV
- ✅ Giao diện web hiện đại, dễ sử dụng

## 💻 Yêu Cầu Hệ Thống

- **Python**: 3.11.x (hoặc 3.8+)
- **Hệ điều hành**: Windows 10/11, Linux, macOS
- **Webcam**: Camera để nhận diện thời gian thực
- **RAM**: Tối thiểu 4GB (khuyến nghị 8GB)
- **Dung lượng**: ~500MB cho dependencies

## 🔧 Cài Đặt

### Bước 1: Clone hoặc tải dự án

```bash
# Nếu có git
git clone <repository-url>
cd face_predict

# Hoặc giải nén file zip vào thư mục face_predict
```

### Bước 2: Tạo Virtual Environment

```powershell
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài Đặt Dependencies

**Lưu ý quan trọng về Dlib:**

Dlib cần được cài đặt đặc biệt trên Windows. Xem file `HUONG_DAN_CAI_DLIB.md` để biết chi tiết.

```powershell
# Cài đặt dlib-bin (khuyến nghị)
pip install dlib-bin==19.24.2.post1

# Cài đặt các package khác
pip install -r requirements.txt
```

**Nếu gặp lỗi với dlib trong requirements.txt:**

```powershell
# Cài đặt từng package (bỏ qua dlib)
pip install flask==2.3.3 opencv-python==4.8.0.76 numpy==1.24.3 Pillow==10.0.0 gunicorn==21.2.0
pip install face-recognition==1.3.0 --no-deps
pip install face-recognition-models
```

### Bước 4: Kiểm Tra Cài Đặt

```powershell
python -c "import dlib; import face_recognition; import cv2; print('All packages OK!')"
```

## 📁 Cấu Hình

### Cấu trúc thư mục

Dự án sẽ tự động tạo các thư mục sau khi chạy lần đầu:

```
face_predict/
├── app/                    # Code chính của ứng dụng
│   ├── __init__.py
│   ├── face_recognizer.py  # Module nhận diện khuôn mặt
│   ├── routers.py          # Routes (nếu cần)
│   └── utils.py            # Helper functions
├── dataset/                # Thư mục chứa ảnh học sinh
│   ├── student1/           # Ảnh của học sinh 1
│   └── student2/           # Ảnh của học sinh 2
├── encodings/              # File encodings đã train
│   └── known_faces.pkl     # File pickle chứa encodings
├── attendance/             # File CSV điểm danh
│   └── attendance_YYYY-MM-DD.csv
├── static/                 # CSS, JS, images
│   ├── css/
│   └── js/
├── templates/              # HTML templates
│   ├── index.html
│   ├── realtime.html
│   ├── upload.html
│   └── attendance.html
├── app.py                  # File chính Flask app
├── train.py                # Script train model
└── requirements.txt        # Dependencies
```

## 🚀 Cách Sử Dụng

### 1. Chuẩn Bị Dữ Liệu (Train Model)

#### Cách 1: Upload qua Web Interface

1. Chạy ứng dụng (xem bước dưới)
2. Truy cập: `http://localhost:5000/upload`
3. Nhập tên học sinh và chọn ảnh
4. Upload nhiều ảnh cho mỗi học sinh (khuyến nghị 3-5 ảnh)
5. Nhấn nút "Train Model" sau khi upload xong

#### Cách 2: Thủ Công

1. Tạo thư mục trong `dataset/` với tên học sinh:
   ```powershell
   mkdir dataset\NguyenVanA
   ```

2. Đặt ảnh vào thư mục đó (JPG, PNG):
   ```
   dataset/
   └── NguyenVanA/
       ├── img1.jpg
       ├── img2.jpg
       └── img3.jpg
   ```

3. Chạy train script:
   ```powershell
   python train.py
   ```

### 2. Chạy Ứng Dụng

```powershell
# Đảm bảo venv đã được kích hoạt
venv\Scripts\activate

# Chạy ứng dụng
python app.py
```

Bạn sẽ thấy output:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: ON
```

### 3. Sử Dụng Giao Diện Web

Mở trình duyệt và truy cập: **http://localhost:5000**

#### Trang Chủ (`/`)
- Xem thống kê tổng quan
- Truy cập các tính năng chính

#### Nhận Diện Thời Gian Thực (`/realtime`)
1. Click vào "Nhận Diện Thời Gian Thực"
2. Cho phép trình duyệt truy cập webcam
3. Nhìn thẳng vào camera
4. Hệ thống sẽ tự động nhận diện và điểm danh

#### Upload Ảnh (`/upload`)
1. Nhập tên học sinh
2. Chọn file ảnh
3. Click "Upload Ảnh"
4. Lặp lại với nhiều ảnh
5. Click "Train Model" để cập nhật

#### Báo Cáo Điểm Danh (`/attendance`)
1. Chọn ngày cần xem
2. Xem danh sách học sinh đã điểm danh
3. Xuất CSV nếu cần

## 🎬 Chạy Ứng Dụng

### Quick Start

```powershell
# 1. Kích hoạt venv
venv\Scripts\activate

# 2. Train model (nếu chưa có dữ liệu)
python train.py

# 3. Chạy ứng dụng
python app.py

# 4. Mở trình duyệt: http://localhost:5000
```

### Chạy với Gunicorn (Production)

```powershell
# Windows (sử dụng waitress thay vì gunicorn)
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app

# Linux/Mac
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📊 API Endpoints

### Web Routes
- `GET /` - Trang chủ
- `GET /realtime` - Nhận diện thời gian thực
- `GET /upload` - Trang upload ảnh
- `GET /attendance?date=YYYY-MM-DD` - Báo cáo điểm danh
- `GET /video_feed` - Video stream từ webcam

### API Routes
- `POST /upload` - Upload ảnh học sinh
- `POST /train` - Train model từ dataset
- `GET /api/attendance?date=YYYY-MM-DD` - Lấy dữ liệu điểm danh (JSON)
- `GET /api/stats` - Lấy thống kê (JSON)

## 🐛 Troubleshooting

### Lỗi: "No module named 'dlib'"

**Giải pháp:**
```powershell
pip install dlib-bin==19.24.2.post1
```

Xem file `HUONG_DAN_CAI_DLIB.md` để biết chi tiết.

### Lỗi: "Could not load encodings"

**Giải pháp:**
1. Đảm bảo đã có ảnh trong thư mục `dataset/`
2. Chạy `python train.py` để tạo file encodings
3. Kiểm tra file `encodings/known_faces.pkl` đã tồn tại

### Lỗi: Camera không hoạt động

**Giải pháp:**
1. Kiểm tra webcam đã được kết nối
2. Đảm bảo không có ứng dụng khác đang dùng camera
3. Cho phép trình duyệt truy cập camera
4. Thử thay đổi camera index trong `app.py`:
   ```python
   camera = cv2.VideoCapture(1)  # Thử 0, 1, 2...
   ```

### Lỗi: "No trained faces"

**Giải pháp:**
1. Upload ít nhất 1 ảnh học sinh
2. Chạy train model: `python train.py` hoặc dùng nút Train trên web
3. Refresh trang web

### Performance chậm

**Tối ưu:**
1. Giảm độ phân giải camera trong code
2. Sử dụng model "hog" thay vì "cnn" (đã được cấu hình)
3. Giảm số lượng ảnh train (3-5 ảnh mỗi người là đủ)

## 📝 Lưu Ý

- **Bảo mật**: Ứng dụng này chỉ dùng cho môi trường nội bộ, không nên deploy trực tiếp ra internet
- **Privacy**: Đảm bảo có sự đồng ý khi sử dụng ảnh và dữ liệu cá nhân
- **Accuracy**: Độ chính xác phụ thuộc vào chất lượng ảnh và điều kiện ánh sáng
- **Storage**: File CSV điểm danh được lưu trong thư mục `attendance/`

## 🔄 Cập Nhật

### Thêm học sinh mới:
1. Upload ảnh qua web hoặc copy vào `dataset/`
2. Chạy `python train.py` hoặc dùng nút Train trên web
3. Refresh ứng dụng

### Xóa học sinh:
1. Xóa thư mục trong `dataset/`
2. Chạy lại `python train.py`

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra file `HUONG_DAN_CAI_DLIB.md` cho lỗi về dlib
2. Xem log trong terminal khi chạy `python app.py`
3. Kiểm tra các file trong thư mục `attendance/` và `encodings/`

## 📄 License

Dự án này sử dụng các thư viện mã nguồn mở. Vui lòng xem requirements.txt để biết chi tiết.

---

**Chúc bạn sử dụng thành công! 🎉**
