from kivy.uix.screenmanager import Screen
from kivy.app import App


class DashboardScreen(Screen):

    def on_enter(self):
        user = App.get_running_app().user_data

        # user table order:
        # id, username, password, role, student_id, full_name, ...

        role = user[3]
        name = user[5] if user[5] else user[1]

        self.ids.info.text = f"Welcome {name} ({role})"

        # ================= STAFF CHECK =================
        is_staff = role in ("HOD", "Warden", "Principal")
        is_student = role == "Student"

        # ===== Approvals button (ONLY staff) =====
        self.ids.approvals_btn.opacity = 1 if is_staff else 0
        self.ids.approvals_btn.disabled = not is_staff

        # ===== Register Student button (ONLY staff) =====
        self.ids.register_btn.opacity = 1 if is_staff else 0
        self.ids.register_btn.disabled = not is_staff

        # ===== Profile button (ONLY student) =====
        self.ids.profile_btn.opacity = 1 if is_student else 0
        self.ids.profile_btn.disabled = not is_student

    # ================= NAVIGATION =================
    def go_apply(self):
        self.manager.current = "apply"

    def go_history(self):
        self.manager.current = "history"

    def go_approvals(self):
        self.manager.current = "approvals"

    def go_register(self):
        self.manager.current = "register"

    def go_profile(self):
        self.manager.current = "profile"

    def logout(self):
        self.manager.current = "login"
