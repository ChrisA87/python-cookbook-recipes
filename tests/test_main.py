import pytest
from recipes.__main__ import main


def test_main_with_no_args_lists_recipes(capsys):
    with pytest.raises(SystemExit) as exc:
        main([])
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert ' 1) Data Structures And Algorithms' in out
    assert ' 2) Strings And Text' in out


@pytest.mark.parametrize('argv', [['1', '5'], ['1', '5', '--code'], ['1', '5', '--doc']])
def test_main__recipe_exists(argv, capsys):
    with pytest.raises(SystemExit) as exc:
        main(argv)
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert 'Found recipe:' in out


def test_main__recipe_doesnt_exist(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['100', '20'])
    out, err = capsys.readouterr()
    assert exc.value.code == 0
    assert err == ''
    assert 'Recipe not found' in out
