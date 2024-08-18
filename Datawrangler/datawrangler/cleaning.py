import pandas as pd

def drop_missing_data(df, columns=None):
    """Drop rows with missing data in specified columns."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in df.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
    return df.dropna(subset=columns) if columns else df.dropna()

def fill_missing_data(df, columns, value):
    """Fill missing data in specified columns with a value."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in df.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    return df.fillna({col: value for col in columns})

def remove_duplicates(df, subset=None):
    """Remove duplicate rows based on specified subset of columns."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if subset is not None:
        if not isinstance(subset, list):
            raise TypeError("Subset parameter must be a list.")
        if not all(col in df.columns for col in subset):
            raise ValueError("Some columns specified are not in the DataFrame.")
    return df.drop_duplicates(subset=subset)
