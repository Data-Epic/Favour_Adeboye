import pandas as pd

def add_new_column(df, column_name, value):
    """
    Add a new column to the DataFrame with a specified value.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to which the new column will be added.
    column_name : str
        The name of the new column to be added.
    value : any
        The value to assign to the new column.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the new column added.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or column_name is not a string.
    ValueError
        If the column_name already exists in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column_name, str):
        raise TypeError("Column name must be a string.")
    if column_name in df.columns:
        raise ValueError(f"Column '{column_name}' already exists in the DataFrame.")
    df[column_name] = value
    return df

def filter_rows(df, condition):
    """
    Filter rows in the DataFrame based on a condition.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to filter.
    condition : str
        A query string to filter rows.

    Returns
    -------
    pd.DataFrame
        The filtered DataFrame.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or condition is not a string.
    ValueError
        If the condition fails to filter the rows correctly.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(condition, str):
        raise TypeError("Condition must be a string.")
    try:
        return df.query(condition)
    except Exception as e:
        raise ValueError(f"Failed to filter rows with condition '{condition}': {e}")

def group_and_aggregate(df, group_by, agg_dict):
    """
    Group the DataFrame by specified columns and apply aggregation functions.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to group and aggregate.
    group_by : list
        List of columns to group by.
    agg_dict : dict
        Dictionary specifying the aggregation functions to apply to columns.

    Returns
    -------
    pd.DataFrame
        The grouped and aggregated DataFrame.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame, group_by is not a list, or agg_dict is not a dict.
    ValueError
        If any of the specified columns in group_by are not in the DataFrame.
        If the aggregation fails due to incorrect aggregation dictionary.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(group_by, list):
        raise TypeError("Group by parameter must be a list.")
    if not all(col in df.columns for col in group_by):
        raise ValueError("Some columns specified in group_by are not in the DataFrame.")
    if not isinstance(agg_dict, dict):
        raise TypeError("Aggregation dictionary must be of type dict.")
    try:
        return df.groupby(group_by).agg(agg_dict)
    except Exception as e:
        raise ValueError(f"Failed to group and aggregate data: {e}")
