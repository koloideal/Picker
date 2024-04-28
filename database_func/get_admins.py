import sqlite3
from sqlite3 import Connection, Cursor


async def get_admins() -> list:

    connection: Connection = sqlite3.connect('database/admin_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admin_users 
                     (id int,
                      first_name varchar(50),
                      last_name varchar(50),
                      username varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''SELECT id FROM admin_users''')

    admins_id: list = [id[0] for id in cursor.fetchall()]

    connection.commit()

    cursor.close()
    connection.close()

    return admins_id
