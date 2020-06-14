import locale
import textwrap

import click

from . import __version__, wikipedia

language_code = locale.getdefaultlocale()[0][0:2]


@click.command()
@click.version_option(version=__version__)
@click.option('--lang',
              default=language_code,
              help='Two-letter language code in which get the summary page')
def main(lang):
    """The hypermodern Python project."""
    data = wikipedia.random_page()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
