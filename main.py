"""Code Here"""

import json


def adjust_recipe(recipe, number):
    data = load_recipe(recipe)
    data["servings"] = number
    for i in data["ingredients"]:
        data["ingredients"][i] = int(data["ingredients"][i] / number)
    return data


def load_recipe(recipe):
    if isinstance(recipe, dict):
        return recipe
    return json.loads(recipe)

if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": '
                   '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    print(adjust_recipe(recipe_json, 2))
