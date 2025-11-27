# controller/cv_controller.py
from model.cv_model import CVModel

class CVController:
    def __init__(self):
        self.model = CVModel()
        self.edit_id = None  # jika sedang edit, simpan idnya

    def save_cv(self, data_dict):
        # Jika sedang edit -> update, jika tidak -> insert
        if self.edit_id:
            updated = self.model.update_cv(self.edit_id, data_dict)
            self.edit_id = None
            return ("update", updated)
        else:
            new_id = self.model.insert_cv(data_dict)
            return ("insert", new_id)

    def list_cvs(self):
        return self.model.get_all()

    def get_cv(self, cv_id):
        return self.model.get_by_id(cv_id)

    def set_edit(self, cv_id):
        self.edit_id = cv_id

    def delete_cv(self, cv_id):
        return self.model.delete_cv(cv_id)

    def close(self):
        self.model.close()
