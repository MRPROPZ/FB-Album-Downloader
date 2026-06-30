# 📸 Facebook Album Downloader

ดาวน์โหลดรูปภาพทั้งหมดจากอัลบั้ม Facebook ด้วย **Python + gallery-dl**

---

## 📦 Installation

### 1. ติดตั้ง Python

ดาวน์โหลดและติดตั้ง Python จาก  
https://www.python.org/downloads/

### 2. ติดตั้ง `gallery-dl`

```bash
pip install gallery-dl
```

### 3. เตรียมไฟล์ `cookies.txt`

1. ติดตั้งส่วนขยาย **Get cookies.txt LOCALLY** บน Chrome หรือ Edge
2. ล็อกอิน Facebook ด้วยบัญชีที่สามารถเข้าถึงอัลบั้มที่ต้องการดาวน์โหลด
3. เปิดหน้า Facebook (หน้าใดก็ได้)
4. คลิกไอคอน **Get cookies.txt LOCALLY**
5. กด **Export** หรือ **Download** เพื่อดาวน์โหลดไฟล์ `cookies.txt`
6. นำไฟล์ `cookies.txt` ไปไว้ในโฟลเดอร์เดียวกับ `download.py`

โครงสร้างโปรเจกต์

```text
project/
├── download.py
├── cookies.txt
```

> **หมายเหตุ**
>
> - หากดาวน์โหลดไม่ได้ ให้ล็อกอิน Facebook ใหม่แล้ว Export `cookies.txt` อีกครั้ง
> - ห้ามเผยแพร่หรือแชร์ไฟล์ `cookies.txt` เนื่องจากเป็นข้อมูลสำหรับยืนยันตัวตนของบัญชี Facebook

---

## 🚀 Usage

### 1. แก้ไข URL อัลบั้ม

เปิดไฟล์ `download.py`

```python
ALBUM_URL = "https://www.facebook.com/media/set/?set=YOUR_ALBUM_ID&type=3"
```

### 2. รันโปรแกรม

```bash
python download.py
```

### 3. ผลลัพธ์

รูปภาพทั้งหมดจะถูกดาวน์โหลดไปยังโฟลเดอร์

```text
downloaded_photos/
```
````
