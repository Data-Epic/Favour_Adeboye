import pandas as pd

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
        if not all(isinstance(col, str) for col in subset):
            raise ValueError("All items in the subset list must be strings representing column names.")
        if not all(col in df.columns for col in subset):
            raise ValueError("Some columns specified are not in the DataFrame.")
    return df.drop_duplicates(subset=subset)

# String Manipulation and Cleaning
def clean_text(data, column, to_lowercase=True, remove_whitespace=True, remove_special_chars=True):
    """
    Cleans text data by applying various operations.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the text data to clean.
    column : str
        The name of the column to clean.
    to_lowercase : bool, optional
        If True, converts text to lowercase. Default is True.
    remove_whitespace : bool, optional
        If True, strips leading and trailing whitespace. Default is True.
    remove_special_chars : bool, optional
        If True, removes special characters. Default is True.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the cleaned text column.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame or column is not a string.
    ValueError
        If the specified column does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column, str):
        raise TypeError("Column parameter must be a string.")
    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    
    if to_lowercase:
        data[column] = data[column].str.lower()
    if remove_whitespace:
        data[column] = data[column].str.strip()
    if remove_special_chars:
        data[column] = data[column].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    return data

# Correct Data Formats
def correct_data_formats(data, column, format_func):
    """
    Ensures data consistency by applying a formatting function.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to format.
    column : str
        The name of the column to format.
    format_func : callable
        A function to apply to each element in the column.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the formatted column.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame, column is not a string, or format_func is not callable.
    ValueError
        If the specified column does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column, str):
        raise TypeError("Column parameter must be a string.")
    if not callable(format_func):
        raise TypeError("Format function must be callable.")
    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    
    data[column] = data[column].apply(format_func)
    return data

# Outlier Correction
def correct_outliers(data, column, lower_bound, upper_bound):
    """
    Corrects outlier values that are outside the specified bounds.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to correct.
    column : str
        The name of the column with potential outliers.
    lower_bound : float
        The minimum acceptable value for the column.
    upper_bound : float
        The maximum acceptable value for the column.

    Returns
    -------
    pd.DataFrame
        The DataFrame with outliers corrected.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame or column is not a string.
    ValueError
        If the specified column does not exist in the DataFrame, or if lower_bound and upper_bound are not floats.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column, str):
        raise TypeError("Column parameter must be a string.")
    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    if not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
        raise TypeError("Bounds must be numeric (int or float).")
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than or equal to upper bound.")
    
    data[column] = data[column].clip(lower_bound, upper_bound)
    return data