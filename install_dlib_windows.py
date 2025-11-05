"""
Script để cài đặt Dlib từ repository z-mahmud22/Dlib_Windows_Python3.x
Cập nhật 2024
"""

import sys
import platform
import subprocess
import urllib.request
import os
from pathlib import Path

# Fix encoding cho Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def get_python_version():
    """Lấy phiên bản Python dạng cpXX (vd: cp310, cp311)"""
    version = sys.version_info
    return f"cp{version.major}{version.minor}"

def get_platform_tag():
    """Lấy platform tag cho Windows"""
    arch = platform.architecture()[0]
    if arch == "64bit":
        return "win_amd64"
    else:
        return "win32"

def download_wheel(url, filename):
    """Tải wheel file từ URL"""
    print(f"Đang tải {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"✓ Đã tải thành công: {filename}")
        return True
    except Exception as e:
        print(f"✗ Lỗi khi tải: {e}")
        return False

def install_wheel(filename):
    """Cài đặt wheel file bằng pip"""
    print(f"Đang cài đặt {filename}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", filename])
        print(f"✓ Đã cài đặt thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Lỗi khi cài đặt: {e}")
        return False

def main():
    python_tag = get_python_version()
    platform_tag = get_platform_tag()
    
    print("=" * 60)
    print("CÀI ĐẶT DLIB TỪ z-mahmud22/Dlib_Windows_Python3.x")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print(f"Python tag: {python_tag}")
    print(f"Platform: {platform_tag}")
    print("=" * 60)
    
    # Dlib version từ requirements.txt
    dlib_version = "19.24.2"
    
    # Tên file wheel
    wheel_filename = f"dlib-{dlib_version}-{python_tag}-{python_tag}-{platform_tag}.whl"
    
    # URL GitHub - thử các URL khả thi
    # Repository này thường có releases với tag khác nhau
    github_urls = [
        f"https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases/download/v{dlib_version}/{wheel_filename}",
        f"https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases/latest/download/{wheel_filename}",
        f"https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/main/{wheel_filename}"
    ]
    
    print(f"\nTên file wheel cần tìm: {wheel_filename}")
    print(f"\nPython 3.11.5 - Tag: {python_tag}")
    print("\nVui lòng tải file từ: https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases")
    print(f"\nTìm file: {wheel_filename}")
    
    # Kiểm tra xem file đã tồn tại chưa
    if os.path.exists(wheel_filename):
        print(f"✓ File {wheel_filename} đã tồn tại, bỏ qua bước tải.")
        install_wheel(wheel_filename)
    else:
        print("\n⚠ File wheel chưa có trong thư mục hiện tại.")
        print("Hãy làm theo các bước sau:")
        print("1. Truy cập: https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases")
        print(f"2. Tìm và tải file: {wheel_filename}")
        print(f"3. Đặt file vào thư mục: {os.getcwd()}")
        print(f"4. Chạy lại script này hoặc chạy: pip install {wheel_filename}")
        
        # Thử tải từ các URL khả thi
        downloaded = False
        for url in github_urls:
            print(f"\nĐang thử tải từ: {url}")
            if download_wheel(url, wheel_filename):
                downloaded = True
                break
        
        if downloaded:
            # Cài đặt
            if install_wheel(wheel_filename):
                # Xóa file sau khi cài đặt thành công
                try:
                    os.remove(wheel_filename)
                    print(f"✓ Đã xóa file tạm: {wheel_filename}")
                except:
                    pass
        else:
            print("\n❌ Không thể tải tự động. Vui lòng tải thủ công từ GitHub releases.")
    
    # Kiểm tra cài đặt
    print("\n" + "=" * 60)
    print("KIỂM TRA CÀI ĐẶT")
    print("=" * 60)
    try:
        import dlib
        print(f"✓ Dlib đã được cài đặt thành công!")
        print(f"  Version: {dlib.__version__}")
    except ImportError:
        print("✗ Không thể import dlib. Vui lòng kiểm tra lại.")
        print("\nHƯỚNG DẪN THỦ CÔNG:")
        print("1. Truy cập: https://github.com/z-mahmud22/Dlib_Windows_Python3.x/releases")
        print(f"2. Tìm file wheel phù hợp với Python {python_tag}")
        print(f"3. Tải file về và cài đặt bằng lệnh:")
        print(f"   pip install <tên_file>.whl")

if __name__ == "__main__":
    main()

