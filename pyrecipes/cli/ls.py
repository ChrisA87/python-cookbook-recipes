import click
from pyrecipes.chapter import Chapter
from pyrecipes.cookbook import cookbook


def render_chapter(chapter: Chapter, describe: bool = False):
    width = len(str(chapter)) + 2
    click.echo(f'{"=" * width}\n{str(chapter):^{width}}\n{"=" * width}')
    for _, recipe in chapter:
        click.echo(f"  {recipe}")
        if describe:
            click.echo(f"    {recipe.get_docstring()}\n")
    click.echo("")


@click.command()
@click.option(
    "-c",
    "--chapter",
    type=int,
    help="List the recipes from a specific chapter",
    multiple=True,
)
@click.option(
    "-d",
    "--describe",
    is_flag=True,
    help="Shows descriptions of the recipes",
)
def ls(chapter, describe):
    """List recipes"""
    if chapter:
        for c in sorted(chapter):
            render_chapter(cookbook[c], describe)
    else:
        for _, chapter in cookbook:
            render_chapter((chapter), describe)
