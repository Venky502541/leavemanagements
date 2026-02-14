from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from database.db import connect_db


class ApprovalScreen(Screen):

    def on_enter(self):
        self.load_pending()

    def load_pending(self):
        self.ids.list.clear_widgets()

        user = App.get_running_app().user_data
        role = user[3]

        con = connect_db()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                leaves.id,
                users.full_name,
                users.student_id,
                leaves.reason,
                leaves.start_date,
                leaves.end_date
            FROM leaves
            JOIN users ON leaves.user_id = users.id
            WHERE leaves.status = 'Pending'
              AND leaves.approver_role = ?
            ORDER BY leaves.id DESC
        """, (role,))

        rows = cur.fetchall()
        con.close()

        if not rows:
            self.ids.list.add_widget(
                Label(
                    text="No pending approvals",
                    size_hint_y=None,
                    height=40
                )
            )
            return

        for r in rows:
            container = BoxLayout(
                orientation="vertical",
                padding=10,
                spacing=8,
                size_hint_y=None
            )
            container.bind(minimum_height=container.setter("height"))

            container.add_widget(Label(
                text=f"[b]{r[1]}[/b] ({r[2]})",
                markup=True,
                size_hint_y=None,
                height=25
            ))

            container.add_widget(Label(
                text=f"{r[3]} | {r[4]} → {r[5]}",
                size_hint_y=None,
                height=22
            ))

            remark_input = TextInput(
                hint_text="Enter remarks (required if rejecting)",
                size_hint_y=None,
                height=40
            )

            btns = BoxLayout(size_hint_y=None, height=40, spacing=10)

            approve = Button(
                text="Approve",
                background_color=(0.1, 0.7, 0.3, 1)
            )
            reject = Button(
                text="Reject",
                background_color=(0.9, 0.2, 0.2, 1)
            )

            approve.bind(
                on_press=lambda x, lid=r[0]: self.update_status(lid, "Approved", "")
            )

            reject.bind(
                on_press=lambda x, lid=r[0], txt=remark_input:
                self.update_status(lid, "Rejected", txt.text)
            )

            btns.add_widget(approve)
            btns.add_widget(reject)

            container.add_widget(remark_input)
            container.add_widget(btns)

            self.ids.list.add_widget(container)

    def update_status(self, leave_id, status, remarks):
        if status == "Rejected" and not remarks.strip():
            return  # remark mandatory for rejection

        con = connect_db()
        cur = con.cursor()

        cur.execute("""
            UPDATE leaves
            SET status = ?, remarks = ?
            WHERE id = ?
        """, (status, remarks, leave_id))

        con.commit()
        con.close()

        self.load_pending()

    def go_back(self):
        self.manager.current = "dashboard"
