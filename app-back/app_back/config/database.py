import sqlite3
from typing import Any
from models import recipes
from constants import database as db_const

_connection = sqlite3.connect(db_const.DATABASE_PATH, check_same_thread=False)
_connection.row_factory = lambda cursor, row: {
    column[0]: row[index] for index, column in enumerate(cursor.description)
}

_cursor = _connection.cursor()


def insert(entity: recipes.Model) -> None:
    entity_dict = entity.dict()
    keys = ",".join(entity_dict.keys())
    values = ",".join(
        [
            "%s"
            % (
                f"'{entity_dict.get(key)}'"
                if type(entity_dict.get(key)) == str
                else entity_dict.get(key)
            )
            for key in keys
        ]
    )
    _cursor.execute(
        "INSERT INTO %s (%s) VALUES (%s)" % (entity.table_name, keys, values)
    )
    _connection.commit()


def fetch(query: str) -> Any:
    _cursor.execute(query)
    rows = _cursor.fetchall()
    return rows
