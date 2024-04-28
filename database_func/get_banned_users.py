import sqlite3
from sqlite3 import Connection, Cursor


async def get_banned_users() -> list:

    connection: Connection = sqlite3.connect('database/banned_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS banned_users 
                     (id int,
                      first_name varchar(50),
                      last_name varchar(50),
                      username varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''SELECT id FROM banned_users''')

    banned_users_id: list = [id[0] for id in cursor.fetchall()]

    connection.commit()

    cursor.close()
    connection.close()

    return banned_users_id
