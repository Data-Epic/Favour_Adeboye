import pandas as pd

def add_new_column(df, column_name, value):
    """Add a new column with a specified value."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column_name, str):
        raise TypeError("Column name must be a string.")
    if column_name in df.columns:
        raise ValueError(f"Column '{column_name}' already exists in the DataFrame.")
    df[column_name] = value
    return df

def filter_rows(df, condition):
    """Filter rows based on a condition."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(condition, str):
        raise TypeError("Condition must be a string.")
    try:
        return df.query(condition)
    except Exception as e:
        raise ValueError(f"Failed to filter rows with condition '{condition}': {e}")

def group_and_aggregate(df, group_by, agg_dict):
    """Group data by specified columns and apply aggregation."""
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
