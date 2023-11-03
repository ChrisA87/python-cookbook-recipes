import sys
from argparse import ArgumentParser
from collections import defaultdict
from typing import List
from recipes import ROOT
from recipes.recipe import Recipe
from .utils import clean_text


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('chapter', nargs='?', type=int)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--code', help='print the recipe code', action='store_true')
    parser.add_argument('--doc', help='print the recipe docstring', action='store_true')
    parser.add_argument('--create', help='create a new recipe skeleton with the name passed to this arg',
                        required=False, metavar='name', type=str)
    return parser.parse_args(argv)


def get_recipes(chapter=None):
    result = defaultdict(list)
    pattern = '**/example.py' if chapter is None else f'{chapter:0>2}*/**/example.py'

    for recipe_path in sorted(ROOT.glob(pattern)):
        recipe = Recipe.from_recipe_path(recipe_path)
        result[recipe.chapter_name].append(recipe)
    return result


def render_recipes(recipes: List[Recipe]):
    if not recipes:
        print('No recipes found')
        return

    print(f"{sum(map(len, recipes.values()))} recipes found")
    for chapter, recipes in recipes.items():
        print(f'\n{clean_text(chapter).title()}\n{"=" * 50}')
        for recipe in recipes:
            print(f'  {clean_text(recipe.name)}')
    print()


def find_chapter_dir(chapter):
    try:
        return next(ROOT.glob(f'{chapter:0>2}_*'))
    except StopIteration:
        print(f'Chapter {chapter} couldn\'t be found')
        sys.exit(0)


def find_recipe_path(args):
    try:
        return next(ROOT.glob(f'**/{args.chapter:0>2}*/{args.number:0>2}*/example.py'))
    except StopIteration:
        print('Recipe not found')
        sys.exit(0)


def get_example_dir(number, name):
    return f"{number:0>2}_{name.lower().replace(' ', '_')}"


def create_new_recipe(args):
    chapter_dir = find_chapter_dir(args.chapter)
    example_dir = chapter_dir.joinpath(get_example_dir(args.number, args.create))
    example_dir.mkdir()
    example_dir.joinpath('example.py').write_text(
        ROOT.joinpath('template.py').read_text())
    print(f'created recipe:\n{example_dir}')
    sys.exit(0)


def main(argv):
    args = parse_args(argv)

    if args.chapter is None or args.number is None:
        render_recipes(get_recipes(args.chapter))
        sys.exit(0)

    if args.create:
        create_new_recipe(args)

    recipe = Recipe(args.chapter, args.number)

    if not recipe.exists():
        print(f'Could not find {recipe}\n')
        sys.exit(0)

    print(f'Found recipe:\n{recipe}\n')

    if args.doc:
        print(recipe.get_docstring())
        sys.exit(0)

    if args.code:
        print(recipe.get_code())
        sys.exit(0)

    recipe.run()
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
