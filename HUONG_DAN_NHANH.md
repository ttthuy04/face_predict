# 🚀 Hướng Dẫn Chạy Nhanh

## Bước 1: Kích hoạt Virtual Environment

```powershell
venv\Scripts\activate
```

## Bước 2: Train Model (Lần đầu tiên)

```powershell
python train.py
```

**Lưu ý:** Cần có ít nhất 1 học sinh trong thư mục `dataset/` với ảnh của họ.

## Bước 3: Chạy Ứng Dụng

```powershell
python app.py
```

## Bước 4: Mở Trình Duyệt

Truy cập: **http://localhost:5000**

---

## 📝 Checklist Trước Khi Chạy

- [ ] Đã cài đặt dlib-bin (xem `HUONG_DAN_CAI_DLIB.md`)
- [ ] Đã cài đặt tất cả packages trong requirements.txt
- [ ] Đã có ít nhất 1 học sinh trong `dataset/` với ảnh
- [ ] Đã train model bằng `python train.py`
- [ ] Webcam đã được kết nối và hoạt động

## 🎯 Các Trang Chính

- **Trang chủ:** http://localhost:5000
- **Nhận diện realtime:** http://localhost:5000/realtime
- **Upload ảnh:** http://localhost:5000/upload
- **Báo cáo điểm danh:** http://localhost:5000/attendance

## ⚠️ Lỗi Thường Gặp

### "No module named 'dlib'"
```powershell
pip install dlib-bin==19.24.2.post1
```

### "Could not load encodings"
```powershell
python train.py
```

### Camera không hoạt động
- Kiểm tra webcam đã kết nối
- Đảm bảo không có app khác đang dùng camera
- Cho phép trình duyệt truy cập camera

---

**Xem `Readme.md` để biết hướng dẫn chi tiết!**

