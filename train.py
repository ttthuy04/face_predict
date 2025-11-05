# train.py
import face_recognition
import pickle
import os
from pathlib import Path

DATASET_DIR = "dataset"
ENCODINGS_FILE = "encodings/known_faces.pkl"

def train():
    """Train face recognition model from dataset"""
    known_encodings = []
    known_names = []
    
    # Kiểm tra thư mục dataset
    if not os.path.exists(DATASET_DIR):
        print(f"Error: Dataset directory '{DATASET_DIR}' not found!")
        print("Please create the directory and add student images.")
        return False
    
    # Lấy danh sách học sinh
    student_folders = [d for d in os.listdir(DATASET_DIR) 
                       if os.path.isdir(os.path.join(DATASET_DIR, d))]
    
    if not student_folders:
        print(f"Error: No student folders found in '{DATASET_DIR}'!")
        print("Please add student folders with images.")
        return False
    
    print(f"Found {len(student_folders)} student(s) to process...")
    print("-" * 50)
    
    total_images = 0
    successful_images = 0
    
    for student_folder in student_folders:
        student_path = os.path.join(DATASET_DIR, student_folder)
        image_files = [f for f in os.listdir(student_path) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not image_files:
            print(f"⚠️  No images found in {student_folder}/")
            continue
        
        print(f"\n📁 Processing {student_folder}...")
        student_encodings_count = 0
        
        for image_file in image_files:
            image_path = os.path.join(student_path, image_file)
            total_images += 1
            
            try:
                # Load và encode ảnh
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                
                if encodings:
                    known_encodings.append(encodings[0])
                    known_names.append(student_folder)
                    student_encodings_count += 1
                    successful_images += 1
                    print(f"  ✅ {image_file} - Face detected")
                else:
                    print(f"  ⚠️  {image_file} - No face detected")
                    
            except Exception as e:
                print(f"  ❌ {image_file} - Error: {e}")
        
        print(f"  📊 {student_folder}: {student_encodings_count}/{len(image_files)} images processed")
    
    # Lưu encodings
    if known_encodings and known_names:
        data = {"encodings": known_encodings, "names": known_names}
        os.makedirs("encodings", exist_ok=True)
        
        with open(ENCODINGS_FILE, "wb") as f:
            pickle.dump(data, f)
        
        print("\n" + "=" * 50)
        print("✅ Training completed successfully!")
        print(f"📊 Total images processed: {successful_images}/{total_images}")
        print(f"👥 Total students: {len(set(known_names))}")
        print(f"💾 Encodings saved to: {ENCODINGS_FILE}")
        return True
    else:
        print("\n❌ Error: No face encodings were created!")
        print("Please check your images and ensure they contain clear faces.")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Face Recognition Training")
    print("=" * 50)
    success = train()
    if not success:
        exit(1)