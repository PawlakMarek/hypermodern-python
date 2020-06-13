import textwrap

import click
import requests

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL) as response:
        try:
            response.raise_for_status()
        except requests.HTTPError:
            click.echo("Wikipedia API is unavailable.\n"
                       "Please check your connection and try again")
            return
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
