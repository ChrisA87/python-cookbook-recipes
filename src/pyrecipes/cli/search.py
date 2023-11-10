import sys
from typing import Mapping
import click
import re
from colorama import Fore, init
from colorama.ansi import AnsiFore
from pyrecipes.chapter import Chapter
from pyrecipes.cookbook import cookbook
from pyrecipes.recipe import SearchMatch
from pyrecipes.utils import text_border

init(autoreset=True)

COLORS = {
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


def get_n_matches(matches):
    count = 0
    for recipes in matches.values():
        for matches in recipes.values():
            count += sum(match.count for match in matches)
    return count


def render_match(
    pattern: str, match: SearchMatch, color: AnsiFore, ignore_case: bool = False
):
    flags = re.IGNORECASE if ignore_case else 0
    text = re.sub(
        pattern,
        lambda match: f"{color}{match.group()}{Fore.RESET}",
        match.line_text,
        flags=flags,
    ).strip()
    click.echo(f"  Line {match.line_number}: {text}")


def render_matches(
    pattern: str,
    match_dict: Mapping[Chapter, Mapping],
    color: AnsiFore,
    ignore_case: bool = False,
):
    for chapter, recipes in match_dict.items():
        click.echo(text_border(str(chapter)))
        for recipe, matches in recipes.items():
            click.echo(f"{chapter.number}.{recipe}")
            for match in matches:
                render_match(pattern, match, color, ignore_case)
            click.echo("")


@click.command()
@click.argument("pattern", type=str)
@click.option(
    "--color",
    type=click.Choice(COLORS.keys(), case_sensitive=False),
    default="red",
    help="Change the color used to highlight matches. The default is red.",
)
@click.option(
    "-i",
    "--ignore-case",
    is_flag=True,
    default=False,
    help="Make the search case-insensitive",
)
@click.option(
    "-c", "--count-only", is_flag=True, help="Return the count of matches only."
)
def search(pattern, color, ignore_case, count_only):
    """Search the recipes for a pattern

    \b
    - RegEx patterns are supported.
    - Searches are case-sensitive by default. Use the `-i` flag to make searches case-insensitive.
    - Use the `-c` flag to display count of matches.

    """
    color = COLORS.get(color)
    match_dict = cookbook.search(pattern, ignore_case)

    click.echo(f"Found {get_n_matches(match_dict):,} matches")

    if count_only:
        sys.exit(0)

    if match_dict:
        render_matches(pattern, match_dict, color, ignore_case)
