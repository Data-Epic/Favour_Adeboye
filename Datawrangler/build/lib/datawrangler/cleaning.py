import pandas as pd

def drop_missing_data(df, columns=None):
    """
    Drop rows with missing data in specified columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame from which to drop rows with missing data.
    columns : list, optional
        List of columns to consider when dropping rows. If None, drops rows where any column is NaN.

    Returns
    -------
    pd.DataFrame
        A DataFrame with rows containing missing data removed.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or columns is not a list.
    ValueError
        If any of the specified columns are not in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in df.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
    return df.dropna(subset=columns) if columns else df.dropna()

def fill_missing_data(df, columns, value):
    """
    Fill missing data in specified columns with a value.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame in which to fill missing data.
    columns : list
        List of columns in which to fill missing data.
    value : any
        The value to use for filling missing data.

    Returns
    -------
    pd.DataFrame
        A DataFrame with missing data filled.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or columns is not a list.
    ValueError
        If any of the specified columns are not in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in df.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    return df.fillna({col: value for col in columns})

def remove_duplicates(df, subset=None):
    """
    Remove duplicate rows based on a specified subset of columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame from which to remove duplicate rows.
    subset : list, optional
        List of columns to consider when identifying duplicates. If None, considers all columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with duplicate rows removed.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or subset is not a list.
    ValueError
        If any of the specified columns in subset are not in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if subset is not None:
        if not isinstance(subset, list):
            raise TypeError("Subset parameter must be a list.")
        if not all(col in df.columns for col in subset):
            raise ValueError("Some columns specified are not in the DataFrame.")
    return df.drop_duplicates(subset=subset)
