export class Ingredient {
  id: string;
  name: string;

  constructor(data: any) {
    this.id = data["id"];
    this.name = data["name"];
  }
}

export class Recipe {
  id: string;
  title: string;
  ingredients: Ingredient[];

  constructor(data: any) {
    this.id = data["id"];
    this.title = data["title"];
    this.ingredients = [];

    data["ingredients"].forEach((ing: any) => {
      this.ingredients.push(new Ingredient(ing));
    });
  }
}
