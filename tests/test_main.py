import pytest
from pyrecipes import __main__ as main
from pyrecipes import template
from tests.conftest import TEMPLATE


def test_main_with_no_args_lists_recipes(capsys):
    with pytest.raises(SystemExit) as exc:
        main.main([])
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert ' 1) Data Structures And Algorithms' in out
    assert ' 2) Strings And Text' in out


@pytest.mark.parametrize('argv', [['1', '5'], ['1', '5', '--code'], ['1', '5', '--doc']])
def test_main__recipe_exists(argv, capsys):
    with pytest.raises(SystemExit) as exc:
        main.main(argv)
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert 'Found recipe:' in out


def test_main__recipe_doesnt_exist(capsys):
    with pytest.raises(SystemExit) as exc:
        main.main(['100', '20'])
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert 'Could not find Recipe(chapter=100, number=20)' in out


def test_template():
    assert template.main() is None


def test_recipes__create__generates_template(recipe_root_dir, capsys, patched_root):

    with pytest.raises(SystemExit) as exc:
        main.main(['1', '2', '--create', 'new test recipe'])
    out, err = capsys.readouterr()
    expected_output_path = recipe_root_dir / '01_test_chapter' / '02_new_test_recipe' / 'example.py'

    assert exc.value.code == 0
    assert err == ''
    assert 'created recipe:' in out
    assert expected_output_path.exists()
    assert expected_output_path.read_text() == TEMPLATE


def test_find_chapter_dir__exists(recipe_root_dir, patched_root):
    chapter = main.find_chapter_dir(1)
    assert chapter == recipe_root_dir / '01_test_chapter'


def test_find_chapter_dir__not_exists(recipe_root_dir, capsys, patched_root):
    with pytest.raises(SystemExit) as exc:
        main.find_chapter_dir(42)
    out, err = capsys.readouterr()

    assert exc.value.code == 0
    assert out == 'Chapter 42 couldn\'t be found\n'
    assert err == ''


def test_render_recipes__no_recipes_found(capsys):
    result = main.render_recipes([])
    out, err = capsys.readouterr()
    assert result is None
    assert err == ''
    assert out == 'No recipes found\n'
