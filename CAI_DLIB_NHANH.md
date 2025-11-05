# Hướng Dẫn Nhanh: Cài Đặt Dlib cho Python 3.11.5

## Bạn đang dùng:
- Python 3.11.5
- Windows 64-bit
- Virtual Environment (venv)

## ⚡ Cách Nhanh Nhất (1 lệnh):

```powershell
# Kích hoạt venv
venv\Scripts\activate

# Cài đặt trực tiếp từ PyPI
pip install dlib-bin==19.24.2.post1
```

## Hoặc Tải Wheel File Thủ Công:

### Phương Pháp 1: Từ PyPI (Khuyến nghị)
1. Truy cập: https://pypi.org/project/dlib-bin/19.24.2.post1/#files
2. Tải: `dlib_bin-19.24.2.post1-cp311-cp311-win_amd64.whl`
3. Cài đặt: `pip install dlib_bin-19.24.2.post1-cp311-cp311-win_amd64.whl`

### Phương Pháp 2: Từ GitHub
1. Truy cập: https://github.com/Silufer/dlib-python
2. Tải: `dlib-19.24.1-cp311-cp311-win_amd64.whl`
3. Cài đặt: `pip install dlib-19.24.1-cp311-cp311-win_amd64.whl`

### Kiểm tra:
```powershell
python -c "import dlib; print(dlib.__version__)"
```

Nếu thấy `19.24.2` → **Thành công!** ✅

---

## Hoặc dùng script tự động:
```powershell
python install_dlib_windows.py
```

