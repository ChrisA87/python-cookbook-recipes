import pytest
from recipes import ROOT


@pytest.fixture(params=list(ROOT.glob('**/example.py')))
def recipe_path(request):
    yield request.param
