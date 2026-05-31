import sqlite3

DATABASE_PATH = "database/users.db"


def create_users_table():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        profession TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()

def create_reviews_table():

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email TEXT NOT NULL,

    filename TEXT NOT NULL,

    pdf_name TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

    conn.commit()

    conn.close()