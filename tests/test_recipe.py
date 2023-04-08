import pytest
from pathlib import Path
from recipes import Recipe


def test_recipe__valid__doesnt_exist__recipe_module_instantiates(capsys):
    recipe = Recipe(Path('./01_testing_chapter/02_testing_example/example.py'))
    recipe.run()
    out, err = capsys.readouterr()

    assert recipe.module == 'example'
    assert recipe.chapter == ' 1) Testing Chapter'
    assert recipe.example == ' 2) Testing example'
    assert recipe.package == ''
    assert 'Couldn\'t find recipe  2) Testing example' in out
    assert err == ''
    with pytest.raises(ModuleNotFoundError, match='This recipe couldn\'t be found:'):
        recipe.get_module()


def test_recipe__invalid_recipe_module_raises_ValueError():
    with pytest.raises(ValueError, match='Expects a recipe module "example.py" - got invalid_path'):
        Recipe(Path('./invalid_path'))


def test_recipes_running(recipe_path, capsys):
    recipe = Recipe(recipe_path)
    recipe.run()

    out, err = capsys.readouterr()
    assert 'TODO' not in recipe.get_docstring()
    assert "if __name__ == '__main__':" in recipe.get_code()
    assert 'Running...' in out
    assert err == ''
