import pandas as pd
import pytest

from data_helpers import add_pct_cols, slugify


@pytest.fixture
def pcts_df():
    columns = [
        'col1',
        'col2',
        'total1',
        'total2',
        'total',
    ]
    data = [
        (50, 60, 200, 300, 100,),
    ]

    return pd.DataFrame.from_records(data, columns=columns)


def test_add_pct_cols(pcts_df):
    df_out = pcts_df.pipe(
        add_pct_cols,
        ['col1', 'col2']
    )

    # Test that output columns appear next to input columns
    cols_out = list(df_out.columns)
    assert cols_out[1] == 'col1_pct'
    assert cols_out[3] == 'col2_pct'

    assert df_out['col1_pct'].iloc[0] == 0.5
    assert df_out['col2_pct'].iloc[0] == 0.6


def test_add_pct_cols_with_suffix(pcts_df):
    df_out = pcts_df.pipe(
        add_pct_cols,
        ['col1', 'col2'],
        suffix='_rate'
    )

    # Test that output columns appear next to input columns
    cols_out = list(df_out.columns)
    assert cols_out[1] == 'col1_rate'
    assert cols_out[3] == 'col2_rate'

    assert df_out['col1_rate'].iloc[0] == 0.5
    assert df_out['col2_rate'].iloc[0] == 0.6


def test_add_pct_cols_multiple_totals(pcts_df):
    df_out = pcts_df.pipe(
        add_pct_cols,
        ['col1', 'col2'],
        total_col=['total1', 'total2']
    )

    # Test that output columns appear next to input columns
    cols_out = list(df_out.columns)
    assert cols_out[1] == 'col1_pct'
    assert cols_out[3] == 'col2_pct'

    assert df_out['col1_pct'].iloc[0] == 0.25
    assert df_out['col2_pct'].iloc[0] == 0.2


def test_slugify():
    assert slugify("Column 1") == "column_1"

    assert slugify("Column - 1") == "column_1"
