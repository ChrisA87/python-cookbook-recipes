from pathlib import Path
from .recipe import Recipe
from typing import List


class CookBook:
    def __init__(self, recipes: List[Recipe]) -> None:
        self.recipes = recipes

    @classmethod
    def from_dir(cls, dir: Path):
        recipes = [
            Recipe.from_recipe_path(recipe_path)
            for recipe_path in sorted(dir.glob("**/example.py"))
        ]
        return cls(recipes)

    @property
    def size(self):
        return len(self.recipes)

    @property
    def tuples(self):
        return tuple((recipe.chapter, recipe.number) for recipe in self.recipes)

    def get_recipes_by_chapter(self, chapter):
        return [recipe for recipe in self.recipes if recipe.chapter == chapter]

    def get_recipe(self, chapter, number):
        results = [
            recipe
            for recipe in self.recipes
            if recipe.chapter == chapter and recipe.number == number
        ]
        return None if not results else results[0]
