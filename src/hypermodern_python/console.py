import locale
import re
import textwrap

import click
import requests

from . import __version__

language_code = locale.getdefaultlocale()[0][0:2]
API_URL = "https://{}.wikipedia.org/api/rest_v1/page/random/summary".format(
    language_code)


@click.command()
@click.version_option(version=__version__)
@click.option('--lang',
              default=language_code,
              help='Two-letter language code in which get the summary page')
def main(lang):
    """The hypermodern Python project."""
    with requests.get(re.sub(r'/[a-z][a-z]\.', '/' + lang + '.',
                             API_URL)) as response:
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException:
            click.echo("Wikipedia API is unavailable.\n"
                       "Please check your connection and try again")
            return 1
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
