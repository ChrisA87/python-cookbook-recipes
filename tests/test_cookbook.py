import pytest
from pyrecipes.cookbook import CookBook


@pytest.fixture
def cookbook(recipe_root_dir):
    yield CookBook.from_dir((recipe_root_dir))


def test_CookBook_init(cookbook):
    assert cookbook.size == 9
    assert cookbook.tuples == (
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    )


@pytest.mark.parametrize("chapter", [1, 2, 3])
def test_CookBook_get_recipes_by_chapter(cookbook, chapter):
    recipes = cookbook.get_recipes_by_chapter(chapter)

    assert len(recipes) == 3
    assert {recipe.number for recipe in recipes} == {1, 2, 3}
    assert {recipe.chapter for recipe in recipes} == {chapter}


def test_CookBook_get_recipe__exists(cookbook):
    recipe = cookbook.get_recipe(1, 2)
    assert recipe.chapter == 1
    assert recipe.number == 2


def test_CookBook_get_recipe__doesnt_exist(cookbook):
    recipe = cookbook.get_recipe(9, 9)
    assert recipe is None
