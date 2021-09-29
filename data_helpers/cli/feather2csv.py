#!/usr/bin/env python

"""Convert a DataFrame saved as a feather file to a CSV"""

import click
import pandas as pd


@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('w'))
def feather2csv(input, output):
    """Convert a DataFrame saved as a feather file to a CSV"""
    data = pd.read_feather(input)
    data.to_csv(output, index=False)


if __name__ == "__main__":
    feather2csv()  # pylint:disable=no-value-for-parameter
