import tkinter as tk
from tkinter import messagebox, ttk
from controller.cv_controller import CVController

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CV Maker - Multi Step Form")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        self.data_cv = {}
        self.controller = CVController()  # controller untuk database

        for F in (PagePersonal, PageEduSkill, PageLangHobby, PageExperience, PagePreview, PageListCV):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PagePersonal)

    def show_frame(self, page):
        self.frames[page].tkraise()

    def populate_forms_from_db_row(self, row):
        """Isi data ke form berdasarkan row database"""
        if not row:
            return

        # Simpan data ke dictionary internal
        self.data_cv["Nama"] = row.get("nama", "")
        self.data_cv["TTL"] = row.get("ttl", "")
        self.data_cv["Alamat"] = row.get("alamat", "")
        self.data_cv["Telepon"] = row.get("telepon", "")
        self.data_cv["Email"] = row.get("email", "")
        self.data_cv["Pendidikan"] = row.get("pendidikan", "")
        self.data_cv["Keahlian"] = row.get("keahlian", "")
        self.data_cv["Bahasa"] = row.get("bahasa", "")
        self.data_cv["Hobi"] = row.get("hobi", "")
        self.data_cv["Pengalaman Kerja"] = row.get("pengalaman", "")

        # Halaman 1
        p = self.frames[PagePersonal]
        for k, entry in p.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, self.data_cv.get(k, ""))

        # Halaman 2
        e = self.frames[PageEduSkill]
        e.txt_pendidikan.delete("1.0", "end")
        e.txt_pendidikan.insert("1.0", self.data_cv["Pendidikan"])

        e.txt_keahlian.delete("1.0", "end")
        e.txt_keahlian.insert("1.0", self.data_cv["Keahlian"])

        # Halaman 3
        l = self.frames[PageLangHobby]
        l.txt_bahasa.delete("1.0", "end")
        l.txt_bahasa.insert("1.0", self.data_cv["Bahasa"])

        l.txt_hobi.delete("1.0", "end")
        l.txt_hobi.insert("1.0", self.data_cv["Hobi"])

        # Halaman 4
        ex = self.frames[PageExperience]
        ex.txt_pengalaman.delete("1.0", "end")
        ex.txt_pengalaman.insert("1.0", self.data_cv["Pengalaman Kerja"])


# ---------------- HALAMAN 1 ---------------- #
class PagePersonal(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="DATA PRIBADI", font=("Arial", 20, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        labels = ["Nama", "TTL", "Alamat", "Telepon", "Email"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(form, width=50)
            entry.grid(row=i, column=1, pady=5)
            self.entries[label] = entry

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Daftar CV",
                  command=lambda: self.root.show_frame(PageListCV)).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Lanjut ➜", bg="green", fg="white",
                  command=self.go_next).pack(side="right", padx=20)

    def go_next(self):
        for key, entry in self.entries.items():
            self.root.data_cv[key] = entry.get().strip()

        if self.root.data_cv["Nama"] == "":
            messagebox.showwarning("Error", "Nama wajib diisi!")
            return

        self.root.show_frame(PageEduSkill)


# ---------------- HALAMAN 2 ---------------- #
class PageEduSkill(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="PENDIDIKAN & KEAHLIAN", font=("Arial", 20, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Pendidikan").grid(row=0, column=0, sticky="w")
        self.txt_pendidikan = tk.Text(form, width=60, height=4)
        self.txt_pendidikan.grid(row=1, column=0, pady=5)

        tk.Label(form, text="Keahlian").grid(row=2, column=0, sticky="w", pady=10)
        self.txt_keahlian = tk.Text(form, width=60, height=4)
        self.txt_keahlian.grid(row=3, column=0)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=20)

        tk.Button(btn_frame, text="⟵ Kembali",
                  command=lambda: self.root.show_frame(PagePersonal)).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Lanjut ➜", bg="green", fg="white",
                  command=self.go_next).pack(side="right", padx=20)

    def go_next(self):
        self.root.data_cv["Pendidikan"] = self.txt_pendidikan.get("1.0", "end").strip()
        self.root.data_cv["Keahlian"] = self.txt_keahlian.get("1.0", "end").strip()
        self.root.show_frame(PageLangHobby)


# ---------------- HALAMAN 3 ---------------- #
class PageLangHobby(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="BAHASA & HOBI", font=("Arial", 20, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Bahasa").grid(row=0, column=0, sticky="w")
        self.txt_bahasa = tk.Text(form, width=60, height=3)
        self.txt_bahasa.grid(row=1, column=0)

        tk.Label(form, text="Hobi").grid(row=2, column=0, sticky="w", pady=10)
        self.txt_hobi = tk.Text(form, width=60, height=3)
        self.txt_hobi.grid(row=3, column=0)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=20)

        tk.Button(btn_frame, text="⟵ Kembali",
                  command=lambda: self.root.show_frame(PageEduSkill)).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Lanjut ➜", bg="green", fg="white",
                  command=self.go_next).pack(side="right", padx=20)

    def go_next(self):
        self.root.data_cv["Bahasa"] = self.txt_bahasa.get("1.0", "end").strip()
        self.root.data_cv["Hobi"] = self.txt_hobi.get("1.0", "end").strip()
        self.root.show_frame(PageExperience)


# ---------------- HALAMAN 4 ---------------- #
class PageExperience(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="PENGALAMAN KERJA", font=("Arial", 20, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Pengalaman Kerja").grid(row=0, column=0, sticky="w")
        self.txt_pengalaman = tk.Text(form, width=60, height=6)
        self.txt_pengalaman.grid(row=1, column=0)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=20)

        tk.Button(btn_frame, text="⟵ Kembali",
                  command=lambda: self.root.show_frame(PageLangHobby)).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Lanjut ➜", bg="green", fg="white",
                  command=self.go_next).pack(side="right", padx=20)

    def go_next(self):
        self.root.data_cv["Pengalaman Kerja"] = self.txt_pengalaman.get("1.0", "end").strip()
        self.root.show_frame(PagePreview)


# ---------------- HALAMAN 5 (PREVIEW & SAVE) ---------------- #
class PagePreview(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="PREVIEW CV", font=("Arial", 20, "bold")).pack(pady=20)

        self.lbl_preview = tk.Label(self, text="", justify="left", font=("Courier", 11))
        self.lbl_preview.pack(pady=10, anchor="w")

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=20)

        tk.Button(btn_frame, text="⟵ Kembali",
                  command=lambda: self.root.show_frame(PageExperience)).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Simpan CV", bg="green", fg="white",
                  command=self.save_cv).pack(side="left", padx=20)

        tk.Button(btn_frame, text="Kirim CV", bg="blue", fg="white",
                  command=self.send_cv).pack(side="right", padx=20)

    def tkraise(self):
        super().tkraise()
        d = self.root.data_cv

        preview_text = f"""
===== DATA PRIBADI =====
Nama: {d.get('Nama','')}
TTL: {d.get('TTL','')}
Alamat: {d.get('Alamat','')}
Telepon: {d.get('Telepon','')}
Email: {d.get('Email','')}

===== PENDIDIKAN =====
{d.get('Pendidikan','')}

===== KEAHLIAN =====
{d.get('Keahlian','')}

===== BAHASA =====
{d.get('Bahasa','')}

===== HOBI =====
{d.get('Hobi','')}

===== PENGALAMAN KERJA =====
{d.get('Pengalaman Kerja','')}
"""
        self.lbl_preview.config(text=preview_text)

    def save_cv(self):
        try:
            res_type, res_val = self.root.controller.save_cv(self.root.data_cv)

            if res_type == "insert":
                messagebox.showinfo("Sukses", f"CV tersimpan ke database (ID: {res_val})")
            else:
                messagebox.showinfo("Sukses", "CV berhasil diperbarui di database.")

            # refresh halaman list CV setelah simpan
            list_page = self.root.frames[PageListCV]
            list_page.refresh_list()

        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan ke database:\n{e}")

    def send_cv(self):
        messagebox.showinfo("Kirim", "CV berhasil dikirim!")


# ---------------- HALAMAN LIST CV ---------------- #
class PageListCV(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.root = root

        tk.Label(self, text="DAFTAR CV", font=("Arial", 20, "bold")).pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("id", "nama", "email", "telepon"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama")
        self.tree.heading("email", text="Email")
        self.tree.heading("telepon", text="Telepon")

        self.tree.column("id", width=40)
        self.tree.column("nama", width=250)
        self.tree.column("email", width=200)
        self.tree.column("telepon", width=100)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=10)

        tk.Button(btn_frame, text="Refresh", command=self.refresh_list).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Tambah Baru", command=self.tambah_baru).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit).pack(side="right", padx=5)
        tk.Button(btn_frame, text="Hapus", command=self.hapus).pack(side="right", padx=5)

        self.refresh_list()

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            rows = self.root.controller.list_cvs()
            for r in rows:
                self.tree.insert("", "end",
                                 values=(r["id"], r["nama"], r["email"], r["telepon"]))
        except Exception as e:
            messagebox.showerror("Error", f"Gagal load CV:\n{e}")

    def get_selected_id(self):
        try:
            selected = self.tree.selection()
            if not selected:
                return None
            return int(self.tree.item(selected[0], "values")[0])
        except:
            return None

    def tambah_baru(self):
        self.root.data_cv = {}
        self.root.controller.edit_id = None
        self.root.show_frame(PagePersonal)

    def edit(self):
        cv_id = self.get_selected_id()
        if not cv_id:
            messagebox.showwarning("Pilih CV", "Pilih data dulu!")
            return

        try:
            data = self.root.controller.get_cv(cv_id)
            self.root.controller.set_edit(cv_id)
            self.root.populate_forms_from_db_row(data)
            self.root.show_frame(PagePersonal)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal load CV:\n{e}")

    def hapus(self):
        cv_id = self.get_selected_id()
        if not cv_id:
            messagebox.showwarning("Pilih CV", "Pilih data dulu!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin ingin dihapus?"):
            return

        try:
            self.root.controller.delete_cv(cv_id)
            messagebox.showinfo("Sukses", "CV berhasil dihapus!")
            self.refresh_list()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal hapus CV:\n{e}")


# ---------------- JALANKAN APLIKASI ---------------- #
if __name__ == "__main__":
    app = MainView()
    app.mainloop()

