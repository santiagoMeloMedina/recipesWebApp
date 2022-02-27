from typing import Any, Dict, List
from models import recipes as recipes_model
from constants import database as db_const
from config import database as db_config


def _parse_recipes(raw_data: List[Dict[str, Any]]) -> Dict[str, recipes_model.Recipe]:
    recipes = {}
    for data in raw_data:
        recipe = recipes_model.Recipe.parse_obj(data)
        recipes[recipe.id] = recipe

    return recipes


def _parse_ingredients_by_recipe(
    raw_data: List[Dict[str, Any]]
) -> Dict[str, recipes_model.Ingredient]:
    recipe_ings: Dict[str, List[recipes_model.IngredientByRecipe]] = {}
    for data in raw_data:
        ingredient = recipes_model.IngredientByRecipe.parse_obj(data)
        if ingredient.recipe_id in recipe_ings:
            recipe_ings[ingredient.recipe_id].append(ingredient)
        else:
            recipe_ings[ingredient.recipe_id] = [ingredient]

    return recipe_ings


def _get_ingredients_by_recipe(recipes: List[recipes_model.Recipe]):
    recipe_ingredients_query = """
        SELECT ings.*, rel.recipe_id FROM %s rel 
        INNER JOIN %s ings 
            ON rel.ingredient_id=ings.id 
        WHERE recipe_id IN (%s)
    """ % (
        db_const.RELATION_TABLE_NAME,
        db_const.INGREDIENTS_TABLE_NAME,
        ",".join([f"'{id}'" for id in recipes]),
    )

    return _parse_ingredients_by_recipe(db_config.fetch(recipe_ingredients_query))


def get_paged_recipes(
    starting: int, limit: int, title: str = None
) -> List[recipes_model.Recipe]:
    title_condition = ""
    if title:
        title_condition = f"WHERE title LIKE '{title.lower()}%'"
    recipies_query = "SELECT * FROM %s %s LIMIT %s, %s" % (
        db_const.RECIPIES_TABLE_NAME,
        title_condition,
        starting,
        limit,
    )
    recipes = _parse_recipes(db_config.fetch(recipies_query))
    ingredients_by_recipe = _get_ingredients_by_recipe(recipes)

    for recipe_id in ingredients_by_recipe:
        ingredients = ingredients_by_recipe.get(recipe_id)
        for ingredient in ingredients:
            recipes.get(recipe_id).ingredients.append(
                recipes_model.Ingredient.parse_obj(ingredient.dict())
            )

    return recipes.values()


def get_paged_recipes_by_ingredient(
    starting: int, limit: int, ingredient: str
) -> List[recipes_model.Recipe]:
    recipies_query = """
        SELECT recp.* FROM %s recp 
        INNER JOIN %s rel 
            ON rel.recipe_id=recp.id 
        WHERE rel.ingredient_id='%s' 
        LIMIT %s, %s""" % (
        db_const.RECIPIES_TABLE_NAME,
        db_const.RELATION_TABLE_NAME,
        ingredient,
        starting,
        limit,
    )
    recipes = _parse_recipes(db_config.fetch(recipies_query))
    ingredients_by_recipe = _get_ingredients_by_recipe(recipes)

    for recipe_id in ingredients_by_recipe:
        ingredients = ingredients_by_recipe.get(recipe_id)
        for ingredient in ingredients:
            recipes.get(recipe_id).ingredients.append(
                recipes_model.Ingredient.parse_obj(ingredient.dict())
            )

    return recipes.values()
