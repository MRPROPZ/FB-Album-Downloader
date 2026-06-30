````markdown
# 📸 Facebook Album Downloader

ดาวน์โหลดรูปภาพทั้งหมดจากอัลบั้ม Facebook ด้วย **Python + gallery-dl**

---

## 📦 Installation

### 1. ติดตั้ง Python
ดาวน์โหลดได้จาก https://www.python.org/downloads/

### 2. ติดตั้ง `gallery-dl`

```bash
pip install gallery-dl
```

### 3. เตรียมไฟล์ Cookies

- ล็อกอิน Facebook บนเบราว์เซอร์
- ใช้ Extension **Get cookies.txt LOCALLY**
- Export เป็นไฟล์ **`cookies.txt`**
- วางไฟล์ไว้ในโฟลเดอร์เดียวกับ `download.py`

โครงสร้างโปรเจกต์

```text
project/
├── download.py
├── cookies.txt
└── README.md
```

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

รูปภาพทั้งหมดจะถูกบันทึกไว้ในโฟลเดอร์

```text
downloaded_photos/
```

---

## ⚠️ หมายเหตุ

- ใช้งานได้กับอัลบั้มที่บัญชี Facebook ของคุณสามารถเข้าถึงได้
- หากดาวน์โหลดไม่สำเร็จ ให้ Export `cookies.txt` ใหม่แล้วลองอีกครั้ง
````
