#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('We lit!')

if __name__ == '__main__':
    hello()