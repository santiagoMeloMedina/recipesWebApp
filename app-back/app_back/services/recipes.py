from typing import Any, Dict, List, Tuple
from repositories import recipes as recipes_repo


def get_paged_recipes(pager_params: Tuple[int, int]) -> List[Dict[str, Any]]:
    recipes = recipes_repo.get_paged_recipes(*pager_params)
    return [recipe.dict() for recipe in recipes]
