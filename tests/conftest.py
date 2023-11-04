import pytest
from pyrecipes import ROOT, __main__


TEMPLATE = (ROOT / 'template.py').read_text()


@pytest.fixture(params=list(ROOT.glob('**/example.py')))
def recipe_path(request):
    yield request.param


@pytest.fixture
def recipe_root_dir(tmp_path_factory):
    root_dir = tmp_path_factory.mktemp('recipes')
    recipe_dir = root_dir / '01_test_chapter' / '01_test_recipe'
    recipe_dir.mkdir(parents=True, exist_ok=True)
    (recipe_dir / 'example.py').write_text(TEMPLATE)
    (root_dir / 'template.py').write_text(TEMPLATE)
    yield root_dir


@pytest.fixture
def patched_root(recipe_root_dir, monkeypatch):
    monkeypatch.setattr(__main__, 'ROOT', recipe_root_dir)
    yield monkeypatch
