from view.main_view import MainView

if __name__ == "__main__":
    try:
        app = MainView()
        app.mainloop()
    except Exception as e:
        print("ERROR TERSEMBUNYI:", e)
        input("Tekan ENTER...")
