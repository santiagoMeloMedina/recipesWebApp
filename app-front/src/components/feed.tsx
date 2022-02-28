import React, { useState } from "react";
import { Ingredient, Recipe } from "./model";
import "./feed.css";
import { ALL_INGREDIENTS, WAIT_FOR_INPUT_TIME } from "../values";

const Feed = (props: {
  recipes: Recipe[];
  ingredients: Ingredient[];
  setByIngredient: any;
  setByNameLike: any;
}) => {
  const [timeout, setTimeouts] = useState<any>(null);

  const changingStopped = (value: string) => {
    if (timeout) clearTimeout(timeout);
    const timer = setTimeout(() => {
      props.setByNameLike(value);
    }, WAIT_FOR_INPUT_TIME);
    setTimeouts(timer);
  };

  return (
    <div className="body">
      <div className="window">
        <div className="inputs">
          <input
            type="text"
            onChange={(event) => {
              changingStopped(event.target.value);
            }}
          />
          <select
            name=""
            id=""
            onChange={(event) => {
              props.setByIngredient(event.target.value);
            }}
          >
            <option value={ALL_INGREDIENTS}>all</option>
            {props.ingredients.map((ing) => (
              <option value={ing.id}>{ing.name}</option>
            ))}
          </select>
        </div>
        <div className="recipes">
          {props.recipes.map((recipe) => (
            <div key={`recipe_${recipe.id}`} className="recipe">
              {/* <div className="image_container">
                                <img src="https://cdn-icons-png.flaticon.com/512/114/114968.png" alt="custom_ingredient" className="ing_image"/>
                            </div> */}
              <div className="content_container">
                <div className="recipe_name">{recipe.title}</div>
                <div className="ingredients">
                  {recipe.ingredients.map((ingredient) => (
                    <div className="ingredient">{ingredient.name}</div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Feed;
