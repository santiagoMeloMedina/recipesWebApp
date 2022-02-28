import sqlite3
from typing import Any
from constants import database as db_const
from threading import Lock

lock = Lock()

def connect_and_get():
    _connection = sqlite3.connect(db_const.DATABASE_PATH, check_same_thread=False)
    _connection.row_factory = lambda cursor, row: {
        column[0]: row[index] for index, column in enumerate(cursor.description)
    }

    return _connection.cursor(), _connection


def fetch(query: str) -> Any:
    _cursor, _conn = connect_and_get()
    _cursor.execute(query)
    rows = _cursor.fetchall()
    _conn.close()
    return rows
