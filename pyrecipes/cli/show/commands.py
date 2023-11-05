import click


@click.group()
def show():
    """Shows things"""


@show.command()
def recipe():
    """Shows a recipe"""
    click.echo("Showing the recipe")
