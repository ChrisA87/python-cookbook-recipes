import click
from .ls import ls
from .chapters import chapters
from .get import get_group
from .search import search_group
from .run import run_group


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def main():
    """The CLI tool to find and display helpful Python recipes."""


main.add_command(ls)
main.add_command(chapters)
main.add_command(get_group)
main.add_command(search_group)
main.add_command(run_group)
