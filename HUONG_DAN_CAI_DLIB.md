# Hướng Dẫn Cài Đặt Dlib trên Windows (2024)

## ⚠️ Lưu ý: Repository z-mahmud22/Dlib_Windows_Python3.x không tồn tại hoặc không có releases

## Các Nguồn Thay Thế Để Tải Dlib Wheel File:

### Phương Pháp 1: Sử dụng dlib-bin từ PyPI (Khuyến nghị - Dễ nhất)

```powershell
# Đảm bảo venv đã được kích hoạt
venv\Scripts\activate

# Cài đặt trực tiếp từ PyPI
pip install dlib-bin==19.24.2.post1
```

Hoặc nếu muốn tải wheel file về:
1. Truy cập: https://pypi.org/project/dlib-bin/19.24.2.post1/#files
2. Tải file: `dlib_bin-19.24.2.post1-cp311-cp311-win_amd64.whl`
3. Cài đặt: `pip install dlib_bin-19.24.2.post1-cp311-cp311-win_amd64.whl`

### Phương Pháp 2: Tải từ GitHub (Silufer/dlib-python)

1. **Truy cập GitHub:**
   ```
   https://github.com/Silufer/dlib-python
   ```
   
2. **Tải file wheel:**
   - Tìm file: `dlib-19.24.1-cp311-cp311-win_amd64.whl`
   - Hoặc truy cập trực tiếp:
   ```
   https://github.com/Silufer/dlib-python/blob/main/dlib-19.24.1-cp311-cp311-win_amd64.whl
   ```
   - Click nút "Download" hoặc "Raw" để tải về

3. **Cài đặt:**
   ```powershell
   pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
   ```

### Phương Pháp 3: Tải từ Hugging Face

1. **Truy cập:**
   ```
   https://huggingface.co/hanamizuki-ai/pypi-wheels/tree/main/dlib
   ```
   
2. **Tìm và tải file:** `dlib-19.24.1-cp311-cp311-win_amd64.whl`

3. **Cài đặt:**
   ```powershell
   pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
   ```

### Phương Pháp 4: Thủ Công (Tìm kiếm trên web)

#### Bước 1: Xác định phiên bản Python

```powershell
python --version
```

**Kết quả hiện tại của bạn:**
- Python: 3.11.5
- Architecture: 64-bit (win_amd64)
- Tag: cp311

#### Bước 2: Tìm Wheel File Phù Hợp

Tìm kiếm trên Google với từ khóa:
```
dlib 19.24 python 3.11 windows wheel cp311 win_amd64 download
```

Hoặc truy cập các trang sau:
- **PyPI dlib-bin:** https://pypi.org/project/dlib-bin/
- **GitHub Silufer:** https://github.com/Silufer/dlib-python
- **Hugging Face:** https://huggingface.co/hanamizuki-ai/pypi-wheels/tree/main/dlib

#### Bước 3: Tải Wheel File

Tìm file wheel có định dạng:
```
dlib-19.24.1-cp311-cp311-win_amd64.whl
```
hoặc
```
dlib_bin-19.24.2.post1-cp311-cp311-win_amd64.whl
```

**Lưu ý:** 
- File wheel cho Python 3.11.5 sẽ có tag `cp311`
- Đảm bảo tải đúng file cho Windows 64-bit (`win_amd64`)

**Các phiên bản Python thường được hỗ trợ:**
- Python 3.8 (cp38)
- Python 3.9 (cp39)
- Python 3.10 (cp310)
- Python 3.11 (cp311)
- Python 3.12 (cp312)

#### Bước 4: Cài Đặt Wheel File

1. **Tải file về thư mục dự án:**
   ```powershell
   cd C:\Documen\AI\face_predict
   ```

2. **Cài đặt bằng pip:**
   ```powershell
   pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
   ```
   
   Hoặc nếu file ở thư mục khác:
   ```powershell
   pip install "C:\path\to\dlib-19.24.1-cp311-cp311-win_amd64.whl"
   ```

#### Bước 5: Xác Nhận Cài Đặt

```powershell
python -c "import dlib; print(dlib.__version__)"
```

Kết quả mong đợi: `19.24.1` hoặc `19.24.2` (tùy phiên bản bạn đã cài)

### Khắc Phục Sự Cố

#### Nếu không tìm thấy wheel cho Python 3.11:

**Giải pháp 1:** Kiểm tra lại releases trên GitHub
- Repository này thường có wheel cho Python 3.11
- Tìm file có tag `cp311` trong releases

**Giải pháp 2:** Thử các phiên bản tương thích
```powershell
# Nếu có wheel cho Python 3.10 hoặc 3.12, có thể thử
pip install dlib-19.24.2-cp310-cp310-win_amd64.whl --force-reinstall --no-deps
```

#### Lỗi: "pip install dlib: No matching distribution found"

- Kiểm tra lại phiên bản Python: `python --version`
- Đảm bảo đã tải đúng wheel file cho phiên bản Python của bạn
- Thử cài đặt với `--no-cache-dir`:
  ```powershell
  pip install dlib-19.24.2-cp313-cp313-win_amd64.whl --no-cache-dir
  ```

#### Lỗi: "ImportError: DLL load failed"

- Cài đặt Visual C++ Redistributable: https://aka.ms/vs/17/release/vc_redist.x64.exe
- Đảm bảo đã cài đặt đầy đủ các dependencies:
  ```powershell
  pip install cmake numpy
  ```

### Kiểm Tra Sau Khi Cài Đặt

```python
import dlib
import face_recognition

print(f"Dlib version: {dlib.__version__}")
print("✓ Dlib đã được cài đặt thành công!")
```

### Thông Tin Tham Khảo

- **PyPI dlib-bin:** https://pypi.org/project/dlib-bin/
- **GitHub Silufer/dlib-python:** https://github.com/Silufer/dlib-python
- **Hugging Face Wheels:** https://huggingface.co/hanamizuki-ai/pypi-wheels/tree/main/dlib
- **Dlib Documentation:** http://dlib.net/

### Ghi Chú

- **dlib-bin** là package chính thức trên PyPI, được khuyến nghị sử dụng
- Các wheel files đã được build sẵn cho Windows, giúp tránh việc phải compile từ source code
- Phiên bản 19.24.1 và 19.24.2 đều tương thích với face-recognition 1.3.0
- Nếu gặp vấn đề, hãy thử cài đặt Visual C++ Redistributable

