import sqlite3

def init_db():

    conn = sqlite3.connect("leads.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        company TEXT,
        role TEXT
    )
    """)

    conn.close()


def save_lead(email, company, role):

    conn = sqlite3.connect("leads.db")

    conn.execute(
        "INSERT INTO leads (email, company, role) VALUES (?, ?, ?)",
        (email, company, role)
    )

    conn.commit()
    conn.close()