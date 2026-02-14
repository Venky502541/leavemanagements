from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.apply_leave import ApplyLeaveScreen
from screens.leave_history import LeaveHistoryScreen
from screens.approvals import ApprovalScreen
from screens.register import RegisterScreen

from database.db import create_tables
from screens.profile import ProfileScreen
# ===== LOAD ALL KV FILES =====
Builder.load_file("kv/login.kv")
Builder.load_file("kv/dashboard.kv")
Builder.load_file("kv/apply_leave.kv")
Builder.load_file("kv/leave_history.kv")
Builder.load_file("kv/approvals.kv")
Builder.load_file("kv/register.kv")
Builder.load_file("kv/profile.kv")

# ===== IMPORT ALL SCREENS =====



class StudentLeaveApp(App):
    user_data = None   # holds logged-in user row

    def build(self):
        create_tables()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ApplyLeaveScreen(name="apply"))
        sm.add_widget(LeaveHistoryScreen(name="history"))
        sm.add_widget(ApprovalScreen(name="approvals"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.current = "login"
        return sm


if __name__ == "__main__":
    StudentLeaveApp().run()
