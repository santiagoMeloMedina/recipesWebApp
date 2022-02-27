import sqlite3
from typing import Any
from models import recipes
from constants import database as db_const

_connection = sqlite3.connect(db_const.DATABASE_PATH, check_same_thread=False)
_connection.row_factory = lambda cursor, row: {
    column[0]: row[index] for index, column in enumerate(cursor.description)
}

_cursor = _connection.cursor()


def fetch(query: str) -> Any:
    _cursor.execute(query)
    rows = _cursor.fetchall()
    return rows
