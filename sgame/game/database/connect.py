import mysql.connector
from typing import Any
from mysql.connector.cursor_cext import MySQLCursorAbstract
from mysql.connector.connection_cext import MySQLConnectionAbstract
from sgame.consts import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


def connect() -> tuple[MySQLConnectionAbstract | Any, MySQLCursorAbstract]:
    # Connect to MySQL
    conn: MySQLConnectionAbstract | Any = mysql.connector.connect(
        host="localhost",
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME,
    )

    cursor: MySQLCursorAbstract = conn.cursor()
    return conn, cursor
