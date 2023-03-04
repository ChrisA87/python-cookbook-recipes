import sys
import pytest
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.append(ROOT)


@pytest.fixture(params=list(ROOT.glob('**/example.py')))
def recipe_path(request):
    yield request.param
