from typing import List
import pydantic
from constants import database as db_const


class Model(pydantic.BaseModel):
    id: str
    table_name: str


class Ingredient(Model):
    name: str

    def __init__(self, *args, **kwargs):
        kwargs.update({"table_name": db_const.INGREDIENTS_TABLE_NAME})
        super().__init__(*args, **kwargs)


class IngredientByRecipe(Ingredient):
    recipe_id: str


class Recipe(Model):
    title: str
    ingredients: List[Ingredient] = list()

    def __init__(self, *args, **kwargs):
        kwargs.update({"table_name": db_const.RECIPIES_TABLE_NAME})
        super().__init__(*args, **kwargs)
