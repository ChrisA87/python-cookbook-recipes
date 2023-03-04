import pytest
from pathlib import Path
from recipes import Recipe
from .conftest import ROOT


def test_recipe__valid_recipe_module_instantiates(recipe_path):
    recipe = Recipe(Path('./01_testing_chapter/02_testing_example/example.py'))
    assert recipe.module == 'example'
    assert recipe.chapter == ' 1) Testing Chapter'
    assert recipe.example == ' 2) Testing example'


def test_recipe__invalid_recipe_module_raises_ValueError():
    with pytest.raises(ValueError, match='Expects a recipe module "example.py" - got invalid_path'):
        Recipe(Path('./invalid_path'))


def test_recipes_running(recipe_path, capsys):
    print(f'HERES THE PATH: {recipe_path}')
    recipe = Recipe(recipe_path)    
    recipe.run()
    
    out, err = capsys.readouterr()
    assert f'Running {recipe}' in out
    assert err == ''
