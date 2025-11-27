# model/cv_model.py
from database.db import get_connection

class CVModel:
    def __init__(self):
        self.conn = get_connection()

    def insert_cv(self, data):
        sql = """
        INSERT INTO cv_data
        (nama, ttl, alamat, telepon, email, pendidikan, keahlian, bahasa, hobi, pengalaman)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (
                data.get("Nama",""),
                data.get("TTL",""),
                data.get("Alamat",""),
                data.get("Telepon",""),
                data.get("Email",""),
                data.get("Pendidikan",""),
                data.get("Keahlian",""),
                data.get("Bahasa",""),
                data.get("Hobi",""),
                data.get("Pengalaman Kerja","")
            ))
        self.conn.commit()
        return cur.lastrowid

    def get_all(self):
        sql = "SELECT * FROM cv_data ORDER BY id DESC"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        return rows

    def get_by_id(self, cv_id):
        sql = "SELECT * FROM cv_data WHERE id=%s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (cv_id,))
            row = cur.fetchone()
        return row

    def update_cv(self, cv_id, data):
        sql = """
        UPDATE cv_data SET
        nama=%s, ttl=%s, alamat=%s, telepon=%s, email=%s,
        pendidikan=%s, keahlian=%s, bahasa=%s, hobi=%s, pengalaman=%s
        WHERE id=%s
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (
                data.get("Nama",""),
                data.get("TTL",""),
                data.get("Alamat",""),
                data.get("Telepon",""),
                data.get("Email",""),
                data.get("Pendidikan",""),
                data.get("Keahlian",""),
                data.get("Bahasa",""),
                data.get("Hobi",""),
                data.get("Pengalaman Kerja",""),
                cv_id
            ))
        self.conn.commit()
        return cur.rowcount

    def delete_cv(self, cv_id):
        sql = "DELETE FROM cv_data WHERE id=%s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (cv_id,))
        self.conn.commit()
        return cur.rowcount

    def close(self):
        try:
            self.conn.close()
        except:
            pass


