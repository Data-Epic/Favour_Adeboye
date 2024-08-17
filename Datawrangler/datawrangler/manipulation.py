import pandas as pd

def add_new_column(df, column_name, value):
    """Add a new column with a specified value."""
    df[column_name] = value
    return df

def filter_rows(df, condition):
    """Filter rows based on a condition."""
    return df.query(condition)

def group_and_aggregate(df, group_by, agg_dict):
    """Group data by specified columns and apply aggregation."""
    return df.groupby(group_by).agg(agg_dict)