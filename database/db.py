import sqlite3

DB_NAME = "leave.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    con = connect_db()
    cur = con.cursor()

    # ================= USERS TABLE =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT,

        student_id TEXT,
        full_name TEXT,
        gender TEXT,

        branch TEXT,
        class_section TEXT,
        year INTEGER,

        mobile TEXT,
        address TEXT,
        parent_name TEXT,
        parent_mobile TEXT
    )
    """)

    # ================= LEAVES TABLE (FINAL) =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leaves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        reason TEXT,
        start_date TEXT,
        end_date TEXT,
        description TEXT,
        status TEXT,
        approver_role TEXT,
        remarks TEXT
    )
    """)

    # ================= DEFAULT STAFF USERS =================
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.executemany("""
        INSERT INTO users
        (username, password, role, full_name)
        VALUES (?, ?, ?, ?)
        """, [
            ("hod1", "1234", "HOD", "HOD User"),
            ("warden1", "1234", "Warden", "Warden User"),
            ("principal1", "1234", "Principal", "Principal User")
        ])

    con.commit()
    con.close()
