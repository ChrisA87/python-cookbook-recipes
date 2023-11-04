import click


@click.group()
def ls():
    """Lists things"""


@ls.command()
@click.argument("chapter", type=int, required=False, default=None)
def recipes(chapter):
    """List recipes"""
    if chapter is None:
        click.echo("listing all recipes")
    else:
        click.echo(f"listing all recipes from chapter {chapter}")


@ls.command()
def chapters():
    """List chapters"""
    click.echo("listing chapters")
