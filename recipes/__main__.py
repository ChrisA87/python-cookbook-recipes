import sys
from pathlib import Path
from argparse import ArgumentParser
from collections import defaultdict
from recipes import Recipe

ROOT = Path(__file__).parent


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('chapter', nargs='?', type=int)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--code', help='print the recipe code', action='store_true')
    parser.add_argument('--doc', help='print the recipe docstring', action='store_true')

    args = parser.parse_args(argv)
    if args.chapter is None or args.number is None:
        render_recipes(get_recipes())
        sys.exit(0)
    return args


def get_recipes():
    result = defaultdict(list)

    for recipe_path in sorted(ROOT.glob('**/example.py')):
        recipe = Recipe(recipe_path)
        result[recipe.chapter].append(recipe)
    return result


def render_recipes(recipes):
    for chapter, recipes in recipes.items():
        print(chapter)
        print('=' * 50)
        for recipe in recipes:
            print(f'  {recipe.example}')
        print()


def find_recipe_path(args):
    try:
        return next(ROOT.glob(f'**/{args.chapter:0>2}*/{args.number:0>2}*/example.py'))
    except StopIteration:
        print('Recipe not found')
        sys.exit(0)


def main(argv):
    args = parse_args(argv)
    recipe = Recipe(find_recipe_path(args))

    print(f'Found recipe:\n{recipe}')
    print(recipe.get_docstring())

    if args.doc:
        sys.exit(0)

    if args.code:
        print(recipe.get_code())
        sys.exit(0)

    recipe.run()
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
