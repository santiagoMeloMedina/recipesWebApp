import sqlite3
from constants import database as db_const
import uuid

conn = sqlite3.connect(db_const.DATABASE_PATH)
cursor = conn.cursor()


MAPPED_INGREDIENTS = {
    "peanut butter and jelly sandwich": ["peanut butter", "jelly", "bread"],
    "buckeyes": ["chocolate", "peanut butter", "sugar"],
    "hawaiian pizza": ["cheese", "pizza dough", "tomato sauce", "pineapple", "bacon"],
    "hot chocolate": ["milk", "chocolate", "sugar"],
    "grilled cheese sandwich": ["bread", "cheese"],
}


def _add_id(mapped, value):
    added = False
    while not added:
        new_id = uuid.uuid4()
        if new_id not in mapped:
            mapped[new_id] = value
            added = True


def insert_ingredients():
    ingredients = set()
    for ings in MAPPED_INGREDIENTS.values():
        for ing in ings:
            ingredients.add(ing)

    ing_entities = dict()
    for ing in ingredients:
        _add_id(mapped=ing_entities, value=ing)

    for ing in ing_entities:
        cursor.execute(
            """
                INSERT INTO {ingredients_table} (id, name) VALUES ('{id}', '{name}') 
        """.format(
                ingredients_table=db_const.INGREDIENTS_TABLE_NAME,
                id=ing,
                name=ing_entities.get(ing),
            )
        )

    conn.commit()
    return {value: key for key, value in ing_entities.items()}


def insert_recipes():
    recipe_entities = dict()
    for recipe in MAPPED_INGREDIENTS:
        _add_id(mapped=recipe_entities, value=recipe)

    for recipe in recipe_entities:
        cursor.execute(
            """
                INSERT INTO {recipe_table} (id, title) VALUES ('{id}', '{title}') 
        """.format(
                recipe_table=db_const.RECIPIES_TABLE_NAME,
                id=recipe,
                title=recipe_entities.get(recipe).lower(),
            )
        )

    conn.commit()
    return {value: key for key, value in recipe_entities.items()}


def insert_relations(recipe_ids, ingredient_ids):
    for recipe in MAPPED_INGREDIENTS:
        recipe_id = recipe_ids.get(recipe)
        ingredients = MAPPED_INGREDIENTS.get(recipe)

        relations = {}
        for ing in ingredients:
            ing_id = ingredient_ids.get(ing)
            _add_id(relations, {"recipe_id": recipe_id, "ingredient_id": ing_id})

        for relation in relations:
            cursor.execute(
                """
                    INSERT INTO {relation_table} (id, recipe_id, ingredient_id) VALUES ('{id}', '{recipe_id}', '{ingredient_id}') 
            """.format(
                    relation_table=db_const.RELATION_TABLE_NAME,
                    id=relation,
                    recipe_id=relations.get(relation).get("recipe_id"),
                    ingredient_id=relations.get(relation).get("ingredient_id"),
                )
            )

    conn.commit()


ingredients = insert_ingredients()

recipes = insert_recipes()

insert_relations(recipes, ingredients)
