from typing import Mapping
import click
import re
from colorama import Fore, init
from pyrecipes.chapter import Chapter
from pyrecipes.cookbook import cookbook
from pyrecipes.recipe import SearchMatch
from pyrecipes.utils import text_border

init(autoreset=True)

COLOURS = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "none": Fore.RESET,
}


def render_match(pattern: str, match: SearchMatch, color=Fore.RED):
    text = re.sub(
        re.compile(pattern), color + pattern + Fore.RESET, match.line_text
    ).strip()
    click.echo(f"  Line {match.line_number}: {text}")


def render_matches(pattern: str, match_dict: Mapping[Chapter, Mapping]):
    for chapter, recipes in match_dict.items():
        click.echo(text_border(str(chapter)))
        for recipe, matches in recipes.items():
            click.echo(recipe)
            for match in matches:
                render_match(pattern, match)
            click.echo("")


@click.command()
@click.argument("pattern", type=str)
@click.option(
    "-c",
    "--color",
    type=click.Choice(COLOURS.keys(), case_sensitive=False),
    default="red",
)
def search(pattern, color):
    """Search the recipes for a pattern"""
    match_dict = cookbook.search(pattern)
    if match_dict:
        render_matches(pattern, match_dict)
    else:
        click.echo(f"No recipes found matching '{pattern}'")
