import sys
import re
from pathlib import Path
from argparse import ArgumentParser


ROOT = Path(__file__).parent.parent


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('chapter', type=int)
    parser.add_argument('number', type=int)
    parser.add_argument('--code', help='print the recipe code', action='store_true')
    return parser.parse_args(argv)


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


def name_cleanser(recipe):
    result = recipe.parent.stem
    result = re.sub(r'[\d_]', ' ', result).strip()
    return result.title()


def recipe_handler(recipe, args):
    if recipe is None:
        print('recipe not found')
    else:
        print(f'Found recipe: {name_cleanser(recipe)}')
        if args.code:
            print(recipe.read_text())


def main(argv):
    args = parse_args(argv)
    recipe = find_recipe(args)
    recipe_handler(recipe, args)

if __name__ == '__main__':
    main(sys.argv[1:])
