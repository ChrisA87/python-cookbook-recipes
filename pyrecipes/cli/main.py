import click
from .list import list_group
from .get import get_group
from .search import search_group
from .run import run_group


@click.group()
def main():
    """The CLI tool to find and display helpful Python recipes."""


main.add_command(list_group)
main.add_command(get_group)
main.add_command(search_group)
main.add_command(run_group)
