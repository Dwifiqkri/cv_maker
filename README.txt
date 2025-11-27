CV Maker (Python + Tkinter)
===========================

😊Aplikasi ini merupakan CV Maker berbasis GUI menggunakan Python (Tkinter) yang dilengkapi dengan:
- Multi halaman (5 halaman input + 1 halaman daftar CV)
- CRUD lengkap (Create, Read, Update, Delete)
- Database MySQL
- Arsitektur MVC (Model – View – Controller)

---

😊 Cara Menjalankan Aplikasi

1. Siapkan Database MySQL
Pastikan MySQL sudah berjalan (misalnya melalui XAMPP).
Buat database dan tabel berikut:

```sql
CREATE DATABASE IF NOT EXISTS cv_maker_db;
USE cv_maker_db;

CREATE TABLE cv_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    ttl VARCHAR(100),
    alamat TEXT,
    telepon VARCHAR(30),
    email VARCHAR(100),
    pendidikan TEXT,
    keahlian TEXT,
    bahasa TEXT,
    hobi TEXT,
    pengalaman TEXT
);

2. Install Library yang Dibutuhkan
Aplikasi membutuhkan library PyMySQL:
nginx
Copy code
pip install pymysql

3. Jalankan Aplikasi
Gunakan perintah:
nginx
Copy code
python main_view.py

Atau jika menggunakan Python 3.12:
nginx
Copy code
py -3.12 main_view.py

😊Struktur Project (MVC)
bash
Copy code
/controller
    cv_controller.py
/model
    cv_model.py
/database
    db.py
main_view.py   ← file utama untuk menjalankan aplikasi

😊Fitur Aplikasi
1. Input data pribadi
2. Input pendidikan & keahlian
3. Input bahasa & hobi
4. Input pengalaman kerja
5. Halaman preview CV
6. Menyimpan data ke database (CREATE)
7. Melihat daftar CV (READ)
8. Mengedit CV (UPDATE)
9. Menghapus CV (DELETE)

😊Pengembang
Nama : Dwi Fiqkri Hermawanto
NIM : 240105016
