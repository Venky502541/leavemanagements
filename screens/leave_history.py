from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from database.db import connect_db


class LeaveHistoryScreen(Screen):

    def on_enter(self):
        self.ids.list.clear_widgets()

        user = App.get_running_app().user_data
        user_id = user[0]

        con = connect_db()
        cur = con.cursor()

        cur.execute("""
            SELECT reason, start_date, end_date, status, remarks
            FROM leaves
            WHERE user_id = ?
            ORDER BY id DESC
        """, (user_id,))

        rows = cur.fetchall()
        con.close()

        if not rows:
            self.ids.list.add_widget(
                Label(text="No leave records found",
                      size_hint_y=None, height=40)
            )
            return

        for r in rows:
            status_color = (1, 0.8, 0, 1)
            if r[3] == "Approved":
                status_color = (0.1, 0.7, 0.3, 1)
            elif r[3] == "Rejected":
                status_color = (0.9, 0.2, 0.2, 1)

            card = BoxLayout(
                orientation="vertical",
                padding=10,
                spacing=5,
                size_hint_y=None
            )
            card.bind(minimum_height=card.setter("height"))

            card.add_widget(Label(
                text=f"[b]Reason:[/b] {r[0]}",
                markup=True,
                size_hint_y=None,
                height=25
            ))

            card.add_widget(Label(
                text=f"{r[1]} → {r[2]}",
                size_hint_y=None,
                height=22
            ))

            card.add_widget(Label(
                text=f"Status: {r[3]}",
                color=status_color,
                size_hint_y=None,
                height=22
            ))

            if r[4]:
                card.add_widget(Label(
                    text=f"Remarks: {r[4]}",
                    size_hint_y=None,
                    height=22
                ))

            self.ids.list.add_widget(card)

    def go_back(self):
        self.manager.current = "dashboard"
