import click
from pyrecipes.cookbook import cookbook


@click.command()
@click.option(
    "-c",
    "--chapter",
    type=int,
    help="List the recipes from a specific chapter",
    multiple=True,
)
def ls(chapter):
    """List recipes"""
    if chapter:
        for chpt in sorted(chapter):
            click.echo(f"listing all recipes from chapter {chpt}")
            click.echo(cookbook.get_recipes_by_chapter(chpt))
    else:
        click.echo("listing all recipes")
        click.echo(cookbook)
