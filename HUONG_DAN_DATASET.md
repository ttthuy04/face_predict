# 📁 Hướng Dẫn Tổ Chức Dataset - Ảnh Học Sinh

## 🎯 Cấu Trúc Thư Mục Dataset

Thư mục `dataset/` có cấu trúc như sau:

```
dataset/
├── NguyenVanA/          # Tên học sinh 1
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   └── img4.jpg
├── TranThiB/            # Tên học sinh 2
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── photo3.jpg
└── LeVanC/              # Tên học sinh 3
    ├── 001.jpg
    ├── 002.jpg
    └── 003.jpg
```

## 📋 Quy Tắc Đặt Tên

### Tên Thư Mục (Tên Học Sinh)
- **Nên dùng:** Tên không có dấu cách đặc biệt
- **Ví dụ tốt:**
  - `NguyenVanA`
  - `TranThiB`
  - `LeVanC`
  - `student1`
  - `John_Doe`
- **Tránh:**
  - `Nguyễn Văn A` (có dấu và khoảng trắng)
  - `Nguyen Van A` (có khoảng trắng - có thể gây lỗi)

### Tên File Ảnh
- **Hỗ trợ định dạng:** `.jpg`, `.jpeg`, `.png`
- **Tên file:** Bất kỳ (không quan trọng)
- **Ví dụ:**
  - `img1.jpg`
  - `photo_001.jpg`
  - `student_face.jpg`

## 📸 Yêu Cầu Về Ảnh

### ✅ Ảnh Tốt (Độ Chính Xác Cao)
- Khuôn mặt rõ ràng, nhìn thẳng camera
- Ánh sáng đầy đủ, không quá tối hoặc quá sáng
- Khuôn mặt chiếm ít nhất 30-50% diện tích ảnh
- Không đeo kính râm, mặt nạ che khuất
- Độ phân giải tối thiểu: 200x200 pixels

### ❌ Ảnh Kém (Độ Chính Xác Thấp)
- Khuôn mặt mờ, không rõ
- Ánh sáng quá tối hoặc quá sáng
- Khuôn mặt quá nhỏ trong ảnh
- Bị che khuất (mặt nạ, tay, vật thể)
- Ảnh group (nhiều người)

### 📊 Số Lượng Ảnh Khuyến Nghị
- **Tối thiểu:** 2-3 ảnh mỗi học sinh
- **Khuyến nghị:** 3-5 ảnh mỗi học sinh
- **Tối đa:** 10-15 ảnh (không cần quá nhiều)

## 🔧 Cách Thêm Ảnh Vào Dataset

### Phương Pháp 1: Copy Thủ Công (Khuyến nghị cho nhiều ảnh)

1. **Tạo thư mục cho học sinh:**
   ```powershell
   # Windows PowerShell
   mkdir dataset\NguyenVanA
   ```

2. **Copy ảnh vào thư mục:**
   - Copy các file ảnh (.jpg, .png) vào thư mục vừa tạo
   - Đặt tên file bất kỳ (ví dụ: `img1.jpg`, `img2.jpg`)

3. **Kiểm tra:**
   ```powershell
   dir dataset\NguyenVanA
   ```

### Phương Pháp 2: Upload Qua Web Interface

1. **Chạy ứng dụng:**
   ```powershell
   python app.py
   ```

2. **Truy cập:** http://localhost:5000/upload

3. **Nhập tên học sinh** (ví dụ: `NguyenVanA`)

4. **Chọn file ảnh** và click "Upload Ảnh"

5. **Lặp lại** với nhiều ảnh cho cùng học sinh

6. **Train model** sau khi upload xong

### Phương Pháp 3: Di Chuyển Ảnh Có Sẵn

Nếu bạn đã có ảnh học sinh ở nơi khác:

```powershell
# Ví dụ: Copy ảnh từ thư mục khác
copy "C:\Photos\Student_A\*.jpg" "dataset\NguyenVanA\"

# Hoặc di chuyển
move "C:\Photos\Student_A\*.jpg" "dataset\NguyenVanA\"
```

## 📝 Ví Dụ Thực Tế

### Ví Dụ 1: Thêm Học Sinh Mới

```powershell
# 1. Tạo thư mục
mkdir dataset\NguyenVanA

# 2. Copy ảnh vào (có thể dùng File Explorer)
# Hoặc dùng lệnh:
copy "D:\Photos\NguyenVanA\*.jpg" "dataset\NguyenVanA\"

# 3. Kiểm tra
dir dataset\NguyenVanA
```

**Kết quả:**
```
dataset/
└── NguyenVanA/
    ├── img1.jpg
    ├── img2.jpg
    ├── img3.jpg
    └── img4.jpg
```

### Ví Dụ 2: Tổ Chức Nhiều Học Sinh

```powershell
# Tạo thư mục cho nhiều học sinh
mkdir dataset\NguyenVanA
mkdir dataset\TranThiB
mkdir dataset\LeVanC

# Copy ảnh tương ứng vào từng thư mục
```

**Kết quả:**
```
dataset/
├── NguyenVanA/
│   ├── img1.jpg
│   └── img2.jpg
├── TranThiB/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── photo3.jpg
└── LeVanC/
    ├── 001.jpg
    └── 002.jpg
```

## 🎓 Sau Khi Thêm Ảnh

### Bước 1: Train Model

```powershell
python train.py
```

Bạn sẽ thấy output:
```
==================================================
🎯 Face Recognition Training
==================================================
Found 3 student(s) to process...
--------------------------------------------------

📁 Processing NguyenVanA...
  ✅ img1.jpg - Face detected
  ✅ img2.jpg - Face detected
  📊 NguyenVanA: 2/2 images processed

📁 Processing TranThiB...
  ✅ photo1.jpg - Face detected
  ✅ photo2.jpg - Face detected
  ✅ photo3.jpg - Face detected
  📊 TranThiB: 3/3 images processed

==================================================
✅ Training completed successfully!
📊 Total images processed: 5/5
👥 Total students: 3
💾 Encodings saved to: encodings/known_faces.pkl
```

### Bước 2: Chạy Ứng Dụng

```powershell
python app.py
```

### Bước 3: Test Nhận Diện

Truy cập: http://localhost:5000/realtime

## ⚠️ Lưu Ý Quan Trọng

1. **Mỗi học sinh = 1 thư mục riêng**
   - ❌ KHÔNG đặt tất cả ảnh vào 1 thư mục
   - ✅ Mỗi học sinh có thư mục riêng

2. **Tên thư mục = Tên hiển thị**
   - Tên thư mục sẽ được dùng làm tên khi nhận diện
   - Ví dụ: `dataset/NguyenVanA/` → sẽ hiển thị "NguyenVanA"

3. **Cần train lại sau khi thêm ảnh mới**
   - Mỗi khi thêm/xóa học sinh hoặc ảnh
   - Chạy `python train.py` để cập nhật model

4. **Chất lượng ảnh quan trọng hơn số lượng**
   - 3 ảnh chất lượng tốt > 10 ảnh chất lượng kém

## 🔍 Kiểm Tra Dataset

### Xem danh sách học sinh:
```powershell
dir dataset
```

### Xem ảnh của 1 học sinh:
```powershell
dir dataset\NguyenVanA
```

### Đếm số ảnh:
```powershell
# Tất cả ảnh trong dataset
Get-ChildItem -Path dataset -Recurse -Include *.jpg,*.jpeg,*.png | Measure-Object | Select-Object Count

# Ảnh của 1 học sinh
(Get-ChildItem -Path "dataset\NguyenVanA" -Include *.jpg,*.jpeg,*.png).Count
```

## 🛠️ Script Hỗ Trợ (Tùy Chọn)

Tạo file `check_dataset.py` để kiểm tra dataset:

```python
import os

dataset_dir = "dataset"
if os.path.exists(dataset_dir):
    students = [d for d in os.listdir(dataset_dir) 
                if os.path.isdir(os.path.join(dataset_dir, d))]
    
    print(f"Tổng số học sinh: {len(students)}")
    for student in students:
        student_path = os.path.join(dataset_dir, student)
        images = [f for f in os.listdir(student_path) 
                 if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        print(f"  {student}: {len(images)} ảnh")
else:
    print("Thư mục dataset không tồn tại!")
```

Chạy: `python check_dataset.py`

---

## 📞 Tóm Tắt

1. **Tạo thư mục:** `dataset/[TênHọcSinh]/`
2. **Đặt ảnh vào:** Copy ảnh vào thư mục đó
3. **Train model:** `python train.py`
4. **Chạy app:** `python app.py`
5. **Test:** Truy cập http://localhost:5000/realtime

**Chúc bạn thành công! 🎉**

