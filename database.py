import sqlite3 as sq

def database():
    conn = sq.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE if not exists users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE if not exists feature_usage(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            pdf_cnt INTEGER DEFAULT 0,
            flashcard_cnt INTEGER DEFAULT 0,
            story_cnt INTEGER DEFAULT 0,
            language_cnt INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()