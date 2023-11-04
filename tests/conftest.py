import pytest
from pyrecipes import ROOT, __main__


TEMPLATE = (ROOT / "template.py").read_text()


@pytest.fixture(params=list(ROOT.glob("**/example.py")))
def recipe_path(request):
    """Iters over every recipe."""
    yield request.param


@pytest.fixture
def recipe_root_dir(tmp_path_factory):
    """Creates dummy recipe dir with chapters 1, 2, 3 each with 3 example recipes."""
    root_dir = tmp_path_factory.mktemp("recipes")
    for i in range(1, 4):
        recipe_dir = root_dir / f"0{i}_test_chapter" / f"0{i}_test_recipe"
        recipe_dir.mkdir(parents=True, exist_ok=True)
        (recipe_dir / "example.py").write_text(TEMPLATE)
        (root_dir / "template.py").write_text(TEMPLATE)
    yield root_dir


@pytest.fixture
def patched_root(recipe_root_dir, monkeypatch):
    """Patches the real root recipe directory for the testing dummy one"""
    monkeypatch.setattr(__main__, "ROOT", recipe_root_dir)
    yield monkeypatch
