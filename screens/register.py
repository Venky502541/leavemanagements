from kivy.uix.screenmanager import Screen
from database.db import connect_db


class RegisterScreen(Screen):

    def register_student(
        self, username, password, student_id, full_name, gender,
        branch, class_section, year, mobile, address, parent_name, parent_mobile
    ):
        if not username or not password or not student_id or not full_name:
            self.ids.msg.text = "Please fill all required fields"
            return

        try:
            con = connect_db()
            cur = con.cursor()

            cur.execute("""
            INSERT INTO users (
                username, password, role,
                student_id, full_name, gender,
                branch, class_section, year,
                mobile, address, parent_name, parent_mobile
            )
            VALUES (?, ?, 'Student', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                username, password,
                student_id, full_name, gender,
                branch, class_section, year,
                mobile, address, parent_name, parent_mobile
            ))

            con.commit()
            con.close()

            self.ids.msg.text = "Student Registered Successfully"
            self.clear_fields()

        except Exception:
            self.ids.msg.text = "Username or Student ID already exists"

    def clear_fields(self):
        for field in [
            "username", "password", "student_id", "full_name", "branch",
            "class_section", "year", "mobile", "address",
            "parent_name", "parent_mobile"
        ]:
            self.ids[field].text = ""

    def go_back(self):
        self.manager.current = "dashboard"
