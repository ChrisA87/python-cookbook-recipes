import click


@click.group()
def search():
    """Searches for a recipe"""
    click.echo("searching for a recipe")


@search.command()
def code():
    """Search code for pattern"""
    click.echo("searching the code for a pattern")


@search.command()
def docs():
    """Search the docstring descriptions for a pattern"""
    click.echo("searching in the docstrings for a pattern")


@search.command()
def all():
    """Search both code and docstrings for a pattern"""
    click.echo("searching everywhere for a pattern")
