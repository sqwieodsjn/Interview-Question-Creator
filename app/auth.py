import sqlite3
import bcrypt

DATABASE_PATH = "database/users.db"


def create_user(
    name,
    profession,
    email,
    password
):

    try:

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        conn = sqlite3.connect(DATABASE_PATH)

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (
                name,
                profession,
                email,
                password
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                name,
                profession,
                email,
                hashed_password.decode()
            )
        )

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:

        return False
def verify_user(
    email,
    password
):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return False

    stored_password = user[0]

    return bcrypt.checkpw(
        password.encode(),
        stored_password.encode()
    )

def get_user_by_email(email):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        name,
        profession,
        email,
        created_at

        FROM users

        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user