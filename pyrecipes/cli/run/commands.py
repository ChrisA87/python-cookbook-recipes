import click


@click.group()
def run():
    """Runs things"""


@run.command()
def recipe():
    """Runs a recipe"""
    click.echo("running the recipe")
