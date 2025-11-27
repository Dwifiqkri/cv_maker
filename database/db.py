# database/db.py
import pymysql

def get_connection():
    """
    Default config untuk XAMPP localhost (root, tanpa password).
    Ubah jika kamu pakai user/password lain.
    """
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="cv_maker_db",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )
