from kivy.uix.screenmanager import Screen
from kivy.app import App
from database.db import connect_db


class ApplyLeaveScreen(Screen):

    def submit_leave(self, reason, start_date, end_date, description):
        # get logged-in user
        user = App.get_running_app().user_data
        user_id = user[0]
        role = user[3]

        # basic validation
        if not reason or not start_date or not end_date:
            self.ids.msg.text = "Please fill all required fields"
            return

        # ================= APPROVAL LOGIC =================
        # Student    → HOD approval
        # HOD/Warden → Principal approval
        # Principal  → Auto-approved
        if role == "Student":
            approver_role = "HOD"
            status = "Pending"

        elif role in ("HOD", "Warden"):
            approver_role = "Principal"
            status = "Pending"

        elif role == "Principal":
            approver_role = "AUTO"
            status = "Approved"

        else:
            self.ids.msg.text = "Invalid role"
            return
        # ==================================================

        try:
            con = connect_db()
            cur = con.cursor()

            cur.execute("""
                INSERT INTO leaves
                (user_id, reason, start_date, end_date, description, status, approver_role)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                reason,
                start_date,
                end_date,
                description,
                status,
                approver_role
            ))

            con.commit()
            con.close()

            # success message
            if role == "Principal":
                self.ids.msg.text = "Leave Applied (Auto Approved)"
            else:
                self.ids.msg.text = "Leave Applied Successfully"

            # clear fields
            self.ids.reason.text = "Select Reason"
            self.ids.start.text = ""
            self.ids.end.text = ""
            self.ids.desc.text = ""

        except Exception as e:
            self.ids.msg.text = "Error applying leave"

    def go_back(self):
        self.manager.current = "dashboard"
