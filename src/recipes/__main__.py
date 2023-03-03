import sys
from pathlib import Path
from argparse import ArgumentParser
from collections import defaultdict
from importlib import import_module


ROOT = Path(__file__).parent.parent


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('chapter', nargs='?', type=int)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--code', help='print the recipe code', action='store_true')

    args = parser.parse_args(argv)
    if args.chapter is None or args.number is None:
        render_recipes(get_recipes())
        sys.exit(0)
    return args


def get_recipes():
    result = defaultdict(list)

    for chapter in sorted(ROOT.iterdir()):
        if chapter.stem[0].isdigit():
            for recipe in sorted(chapter.iterdir()):
                result[chapter.stem].append(recipe.stem)
    return result


def clean_text(text):
    num, text = text.split('_', maxsplit=1)
    return f"{int(num):>2}) {text.replace('_', ' ').capitalize()}"


def render_recipes(recipes):
    for chapter, recipes in recipes.items():
        print(clean_text(chapter).title())
        print('=' * 50)
        for recipe in recipes:
            print(f'  {clean_text(recipe)}')
        print()


def find_recipe(args):
    result = None
    chapter = f'{args.chapter:0>2}'
    number = f'{args.number:0>2}'
    
    chapter_dir = [x for x in ROOT.iterdir() if x.is_dir() and x.stem.startswith(chapter)]
    if chapter_dir:
        recipe_dir = [x for x in chapter_dir[0].iterdir() if x.is_dir() and x.stem.startswith(number)]
        if recipe_dir:
            return recipe_dir[0] / 'example.py'
    return result


def recipe_handler(recipe, args):
    if recipe is None:
        print('No recipe found')
    else:
        print(f'Found recipe: {clean_text(recipe.parent.stem)}\n')
        if args.code:
            print(recipe.read_text())
            sys.exit(0)
        run_recipe(recipe)


def get_chapter_example(recipe):
    return recipe.parent.parent.stem, recipe.parent.stem


def run_recipe(recipe):
    chapter, example = get_chapter_example(recipe)
    module = import_module(f'src.{chapter}.{example}.example')
    func = getattr(module, 'main')
    print('Running...')
    func()


def main(argv):
    args = parse_args(argv)
    recipe = find_recipe(args)
    recipe_handler(recipe, args)


if __name__ == '__main__':
    main(sys.argv[1:])
