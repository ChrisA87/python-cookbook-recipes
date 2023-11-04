import click
from pyrecipes.cookbook import CookBook
from pyrecipes import ROOT


COOKBOOK = CookBook.from_dir(ROOT)


class ClickConfig:
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(ClickConfig, ensure=True)


@click.group()
def main():
    """CLI tool to display with python cookbook recipes."""
    pass


@main.group()
def list():
    """Lists recipes"""
    click.echo("listing")


@main.group()
def get():
    """Gets recipes"""
    click.echo("getting recipe")


@list.command()
def chapters():
    """Lists chapters"""
    click.echo("listing chapters")


@list.command()
def recipes():
    click.echo("listing recipes")


@click.group()
@click.option("--verbose", is_flag=True)
@pass_config
def demo(config, verbose):
    if verbose:
        click.echo("We are in verbose mode")


@demo.command()
@click.option("--string", default="World", help="This is the thing that is greeted")
@click.option("--repeat", default=1, help="How many times you should be greeted")
@click.argument("out", type=click.File("w"), default="-", required=False)
def greet(string, repeat, out):
    """This script greets you"""

    for _ in range(repeat):
        click.echo(f"hello {string}", file=out)


if __name__ == "__main__":
    main()
