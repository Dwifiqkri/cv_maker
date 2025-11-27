CV Maker (Python + Tkinter)
===========================

Instruksi singkat:
1. Buat database & tabel (lihat sql/create table di README).
2. Salin file .env dan isi kredensial MySQL.
3. Install requirement:
   pip install -r requirements.txt
4. Jalankan:
   python main.py

Build .exe (Windows):
1. pip install pyinstaller
2. pyinstaller --onefile --add-data "view;view" --add-data "model;model" --add-data "controller;controller" --add-data "database;database" main.py
3. Hasil di folder dist/main.exe

Catatan:
- Jangan commit file .env ke GitHub.
- Jika koneksi DB error, cek credential, port, dan apakah service MySQL berjalan.
