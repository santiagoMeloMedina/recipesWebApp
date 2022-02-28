import {
  getPagedRecipesUrl,
  getRecipesByIngredientUrl,
  getPagedIngredientsUrl,
  getPagedRecipesByNameLikeUrl,
} from "./values";
import { Ingredient, Recipe } from "./components/model";

const HOST_URL = "http://localhost:5000";

const request = async (
  url: string,
  method: string,
  body?: any
): Promise<any> => {
  const response = await fetch(`${HOST_URL}${url}`, {
    method: method,
    ...(body == undefined
      ? {}
      : {
          body,
        }),
  });
  const data = await response.json();
  return data["message"];
};

const getPagedRecipes = async (): Promise<Recipe[]> => {
  const data = await request(getPagedRecipesUrl, "GET");
  return (data as Array<any>).map((recipe) => {
    return new Recipe(recipe);
  });
};

const getPagedRecipesByNameLike = async (name: string): Promise<Recipe[]> => {
  const data = await request(getPagedRecipesByNameLikeUrl(name), "GET");
  return (data as Array<any>).map((recipe) => {
    return new Recipe(recipe);
  });
};

const getRecipesByIngredient = async (
  ingredient: string
): Promise<Recipe[]> => {
  const data = await request(getRecipesByIngredientUrl(ingredient), "GET");
  return (data as Array<any>).map((recipe) => {
    return new Recipe(recipe);
  });
};

const getPagedIngredients = async (): Promise<Ingredient[]> => {
  const data = await request(getPagedIngredientsUrl, "GET");
  return (data as Array<any>).map((ing) => {
    return new Ingredient(ing);
  });
};

export {
  getPagedRecipes,
  getRecipesByIngredient,
  getPagedIngredients,
  getPagedRecipesByNameLike,
};
