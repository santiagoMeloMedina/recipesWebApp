const PAGE_LIMIT = 50;
export const ALL_INGREDIENTS = "ALL";
export const WAIT_FOR_INPUT_TIME = 500;

export const getPagedRecipesUrl = `/recipes?limit=${PAGE_LIMIT}`;
export const getPagedRecipesByNameLikeUrl = (name) =>
  `/recipes?limit=${PAGE_LIMIT}&name=${name}`;
export const getRecipesByIngredientUrl = (ingredient) =>
  `/recipes/${ingredient}?limit=${PAGE_LIMIT}`;
export const getPagedIngredientsUrl = `/ingredients?limit=${PAGE_LIMIT}`;
