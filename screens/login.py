from kivy.uix.screenmanager import Screen
from kivy.app import App
from database.db import connect_db

class LoginScreen(Screen):

    def do_login(self, username, password, role):
        con = connect_db()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=? AND role=?",
            (username, password, role)
        )

        user = cur.fetchone()
        con.close()

        if user:
            App.get_running_app().user_data = user
            self.manager.current = "dashboard"
        else:
            self.ids.msg.text = "Invalid Login"
