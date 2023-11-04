import click


@click.group()
def get():
    """Gets things"""


@get.command()
def recipe():
    """Gets a recipe"""
    click.echo("getting the recipe")
