from typing import List
import pydantic
from constants import database as db_const


class Model(pydantic.BaseModel):
    id: str


class Ingredient(Model):
    name: str


class IngredientByRecipe(Ingredient):
    recipe_id: str


class Recipe(Model):
    title: str
    ingredients: List[Ingredient] = list()
