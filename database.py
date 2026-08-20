
import sqlite3


DATABASE = "contacts.db"



def create_table():

    conn = sqlite3.connect(
        DATABASE
    )

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
        """
    )


    conn.commit()

    conn.close()




def save_contact(
    name,
    email,
    message
):


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO contacts
        (name,email,message)

        VALUES (?,?,?)
        """,

        (
            name,
            email,
            message
        )
    )


    conn.commit()

    conn.close()




def get_contacts():


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM contacts
        ORDER BY id DESC
        """
    )


    contacts = cursor.fetchall()


    conn.close()


    return contacts

