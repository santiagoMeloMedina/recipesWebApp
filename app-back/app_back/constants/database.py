import os

DATABASE_PATH = "%s/.litedb.db" % (os.path.dirname(os.path.abspath(__name__)))

RECIPIES_TABLE_NAME = "Recipies"
INGREDIENTS_TABLE_NAME = "Ingredients"
RELATION_TABLE_NAME = "Recipies_Ingredients"
