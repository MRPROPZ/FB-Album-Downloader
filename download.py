"""
ดาวน์โหลดรูปทั้งหมดจากอัลบั้ม Facebook ลงโฟลเดอร์
ต้องติดตั้ง gallery-dl ก่อน: pip install gallery-dl
และต้องมีไฟล์ cookies.txt (export จากเบราว์เซอร์ที่ล็อกอิน Facebook อยู่)
"""

import subprocess
import sys
import os

ALBUM_URL = "https://www.facebook.com/media/set/?set=a.1555467848082088&type=3"
OUTPUT_DIR = "downloaded_photos"
COOKIES_FILE = "cookies.txt"


def download_facebook_album(album_url: str, output_dir: str, cookies_file: str):
    if not os.path.exists(cookies_file):
        print(f"ไม่พบไฟล์ {cookies_file} — ต้อง export cookies จากเบราว์เซอร์ที่ล็อกอิน Facebook ก่อน")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    print(f"กำลังดาวน์โหลดอัลบั้มไปที่: {output_dir}")
    result = subprocess.run([sys.executable, "-m", "gallery_dl", ALBUM_URL, "-d", OUTPUT_DIR, "--cookies", COOKIES_FILE])

    if result.returncode == 0:
        count = sum(len(files) for _, _, files in os.walk(output_dir))
        print(f"เสร็จสิ้น ดาวน์โหลดไฟล์ทั้งหมด {count} ไฟล์")
    else:
        print("เกิดข้อผิดพลาด ลองตรวจสอบ:")
        print("- cookies.txt ยังไม่หมดอายุ (ลอง export ใหม่)")
        print("- ลิงก์อัลบั้มถูกต้องและยังเข้าถึงได้")


if __name__ == "__main__":
    download_facebook_album(ALBUM_URL, OUTPUT_DIR, COOKIES_FILE)
