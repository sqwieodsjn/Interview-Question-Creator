import sqlite3


def save_review(
    email,
    filename,
    pdf_name
):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reviews
        (
            email,
            filename,
            pdf_name
        )
        VALUES
        (?, ?, ?)
        """,
        (
            email,
            filename,
            pdf_name
        )
    )

    conn.commit()

    conn.close()

def get_reviews(email):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        filename,
        pdf_name,
        created_at

        FROM reviews

        WHERE email = ?

        ORDER BY id DESC

        LIMIT 10
        """,

        (email,)   # <-- HERE
    )

    data = cursor.fetchall()

    conn.close()

    return data

def get_user_pdf_count(email):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM reviews

        WHERE email = ?
        """,
        (email,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count