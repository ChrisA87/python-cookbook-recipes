import click
from .ls import ls
from .chapters import chapters
from .show import show
from .run import run


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def main():
    """The CLI tool to find and display helpful Python recipes."""


main.add_command(ls)
main.add_command(run)
main.add_command(chapters)
main.add_command(show)
