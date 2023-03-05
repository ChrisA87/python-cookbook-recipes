import sys
from argparse import ArgumentParser
from collections import defaultdict
from recipes import Recipe, ROOT


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('chapter', nargs='?', type=int)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--code', help='print the recipe code', action='store_true')
    parser.add_argument('--doc', help='print the recipe docstring', action='store_true')
    parser.add_argument('--create', help='create a new recipe skeleton with the name passed to this arg',
                        required=False, type=str)

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
        print(f'\n{chapter}\n{"=" * 50}')
        for recipe in recipes:
            print(f'  {recipe.example}')
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
    if args.create:
        create_new_recipe(args)

    recipe = Recipe(find_recipe_path(args))
    print(f'Found recipe:\n{recipe}')

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
