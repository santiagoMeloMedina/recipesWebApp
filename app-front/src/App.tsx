import React, { useEffect, useState } from "react";
import "./App.css";
import {
  getPagedRecipes,
  getRecipesByIngredient,
  getPagedIngredients,
  getPagedRecipesByNameLike,
} from "./client";
import { Ingredient, Recipe } from "./components/model";
import Feed from "./components/feed";
import { ALL_INGREDIENTS } from "./values";

function App() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [ingredients, setIngredients] = useState<Ingredient[]>([]);

  useEffect(() => {
    getPagedRecipes().then((data) => setRecipes(data));
    getPagedIngredients().then((data) => setIngredients(data));
  }, []);

  const getNewRecipesByIngredient = (ingredient: string) => {
    if (ingredient == ALL_INGREDIENTS) {
      getPagedRecipes().then((data) => setRecipes(data));
    } else {
      getRecipesByIngredient(ingredient).then((data) => setRecipes(data));
    }
  };

  const getRecipiesByNameLike = (name: string) => {
    if (name.length > 0) {
      getPagedRecipesByNameLike(name).then((data) => setRecipes(data));
    } else {
      getPagedRecipes().then((data) => setRecipes(data));
    }
  };

  return (
    <Feed
      recipes={recipes}
      ingredients={ingredients}
      setByIngredient={getNewRecipesByIngredient}
      setByNameLike={getRecipiesByNameLike}
    />
  );
}

export default App;
