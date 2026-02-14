from kivy.uix.screenmanager import Screen
from kivy.app import App


class ProfileScreen(Screen):

    def on_enter(self):
        user = App.get_running_app().user_data

        # SAFETY: profile only for students
        if user[3] != "Student":
            self.manager.current = "dashboard"
            return

        # users table order:
        # id, username, password, role,
        # student_id, full_name, gender,
        # branch, class_section, year,
        # mobile, address, parent_name, parent_mobile

        self.ids.name.text = user[5] or "-"
        self.ids.sid.text = user[4] or "-"
        self.ids.gender.text = user[6] or "-"
        self.ids.branch.text = user[7] or "-"
        self.ids.class_section.text = user[8] or "-"
        self.ids.year.text = str(user[9]) if user[9] else "-"
        self.ids.mobile.text = user[10] or "-"
        self.ids.address.text = user[11] or "-"
        self.ids.parent_name.text = user[12] or "-"
        self.ids.parent_mobile.text = user[13] or "-"

    def go_back(self):
        self.manager.current = "dashboard"
