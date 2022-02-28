from typing import Any, Dict, List, Tuple
from repositories import recipes as recipes_repo


def get_paged_recipes(
    pager_params: Tuple[int, int], title: str = None, ingredient: str = None
) -> List[Dict[str, Any]]:
    if not ingredient:
        recipes = recipes_repo.get_paged_recipes(*pager_params, title=title)
    else:
        recipes = recipes_repo.get_paged_recipes_by_ingredient(
            *pager_params, ingredient=ingredient
        )

    return [recipe.dict() for recipe in recipes]

def get_paged_ingredients(
    pager_params: Tuple[int, int]
) -> List[Dict[str, Any]]:
    ings = recipes_repo.get_paged_ingredients(*pager_params)
    return [ing.dict() for ing in ings]