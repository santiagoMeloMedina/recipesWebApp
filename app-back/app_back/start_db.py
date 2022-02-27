import sqlite3
from constants import database as db_const


conn = sqlite3.connect(db_const.DATABASE_PATH)
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS {recipe_table} (
        id VARCHAR(50) PRIMARY KEY,
        title VARCHAR(100) NOT NULL
    )
""".format(
        recipe_table=db_const.RECIPIES_TABLE_NAME
    )
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS {ingredients_table} (
        id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )
""".format(
        ingredients_table=db_const.INGREDIENTS_TABLE_NAME
    )
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS {relation_table} (
        id VARCHAR(50) PRIMARY KEY,
        recipe_id VARCHAR(50),
        ingredient_id VARCHAR(50),
        FOREIGN KEY (ingredient_id) REFERENCES {ingredients_table} (id) 
            ON DELETE CASCADE 
            ON UPDATE NO ACTION,
        FOREIGN KEY (recipe_id) REFERENCES {recipe_table} (id) 
            ON DELETE CASCADE 
            ON UPDATE NO ACTION
    )
""".format(
        recipe_table=db_const.INGREDIENTS_TABLE_NAME,
        ingredients_table=db_const.INGREDIENTS_TABLE_NAME,
        relation_table=db_const.RELATION_TABLE_NAME,
    )
)

conn.commit()
