import re


def add_pct_cols(df, cols, total_col='total', suffix='_pct'):
    """Calculates percentage columns from existing columns.

    Args:
        df: Pandas DataFrame.
        cols: Iterable of column names that will be the numerator of the
            percentage.
        total_col: Name of column that will be the denominator of the
            percentage, or iterable of column names that will be used as
            the denominator for value in `cols` (`cols[i] / total_col[i]`).
            Defaults to 'total'.
        suffix: Suffix that will be added to each column name in `cols` for
            the calculated percentage. Defaults to '_pct'.

    Returns:
        Pandas DataFrame with original columns and calculated percentage
        columns. The calculated percentage columns appear next to the
        column used as the numerator.

    """
    # Create a lookup out of the input column names to both test if it's a
    # column that we need to use to calculate a percentage and to get the
    # index of the numerator and denominator colums.

    col_to_idx = {col: i for i, col in enumerate(cols)}
    # We'll return a copy of the source DataFrame rather than altering it
    # in-place.
    df_out = df.copy()

    # A list of output column names. We use this so we can put the percentage
    # columns next to the column that was used as the numerator.
    cols_out = []

    for col in df.columns:
        # Preserve column ordering for the DataFrame we'll return.
        cols_out.append(col)

        if col not in col_to_idx:
            # We're not calculating a percentage from this column. Just pass
            # it through.
            continue

        if isinstance(total_col, str):
            # total_col is a string. Use it as the denominator for calculating
            # all the rates.
            divisor_col = total_col

        else:
            # Assume total_col is an iterable. Get the denominator
            # corresponding to the current numerator.
            divisor_col = total_col[col_to_idx[col]]

        # Calculate the percentage.
        pct_col = '{}{}'.format(col, suffix)
        df_out[pct_col] = df[col] / df[divisor_col]

        # Add the newly calculated column name to the list of output columns,
        # preserving order.
        cols_out.append(pct_col)

    # Reorder the columns so the calculated perentages.
    return df_out[cols_out]


def slugify(s, sep='_'):
    """Removes whitespace and punctuation from a string."""
    return re.sub(r'[\s\-]+', sep, s.lower())


def normalize_column_name(col_name, lookup=None, prefix=''):
    """
    Normalize column name.

    First, try a lookup table, then just slugify

    """
    if lookup is None:
        lookup = {}

    try:
        slug = lookup[col_name]

    except KeyError:
        slug = slugify(col_name)

    return '{}{}'.format(prefix, slug)


def parse_boolean(val):
    """Returns boolean value corresponding to string, e.g. 'Y' or 'N'"""
    if val in ('Y', "Yes", 1):
        return True
    elif val in ('N', "No", 0):
        return False

    return None 
