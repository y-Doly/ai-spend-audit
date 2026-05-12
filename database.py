import sqlite3

def init_db():

    conn = sqlite3.connect("leads.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS audits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        company TEXT,
        role TEXT,
        total_savings REAL,
        recommendations TEXT
    )
    """)

    conn.close()


def save_audit(email, company, role, total_savings, recommendations):

    conn = sqlite3.connect("leads.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO audits (
        email,
        company,
        role,
        total_savings,
        recommendations
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        email,
        company,
        role,
        total_savings,
        recommendations
    ))

    conn.commit()

    audit_id = cursor.lastrowid

    conn.close()

    return audit_id