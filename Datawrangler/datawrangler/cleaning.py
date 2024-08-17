import pandas as pd

def drop_missing_data(df, columns=None):
    """Drop rows with missing data in specified columns."""
    if columns:
        return df.dropna(subset=columns)
    return df.dropna()

def fill_missing_data(df, columns, value):
    """Fill missing data in specified columns with a value."""
    return df.fillna({col: value for col in columns})

def remove_duplicates(df, subset=None):
    """Remove duplicate rows based on specified subset of columns."""
    return df.drop_duplicates(subset=subset)