import pandas as pd

def validate_data_types(df, expected_types):
    """
    Validates the data types of DataFrame columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    expected_types : dict
        Dictionary of column names and expected data types.

    Returns
    -------
    bool
        True if all columns match expected data types, False otherwise.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or expected_types is not a dictionary.
    ValueError
        If any column specified in expected_types does not exist in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(expected_types, dict):
        raise TypeError("Expected types must be provided as a dictionary.")
    
    for column, dtype in expected_types.items():
        if column not in df.columns:
            raise ValueError(f"Column '{column}' is not in the DataFrame.")
        if not pd.api.types.is_dtype_equal(df[column].dtype, dtype):
            return False
    return True

# Convert to Numeric
def convert_to_numeric(data, columns, errors='coerce'):
    """
    Converts specified columns to numeric types.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the columns to convert.
    columns : list
        List of column names to convert to numeric types.
    errors : {'ignore', 'raise', 'coerce'}, default 'coerce'
        How to handle errors during conversion. 'coerce' will set non-convertible values to NaN.

    Returns
    -------
    pd.DataFrame
        DataFrame with specified columns converted to numeric types.

    Raises
    ------
    TypeError
        If data is not a DataFrame or columns is not a list.
    ValueError
        If any column specified does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    
    for col in columns:
        data[col] = pd.to_numeric(data[col], errors=errors)
    return data

# Convert to Datetime
def convert_to_datetime(data, columns, format=None):
    """
    Converts specified columns to datetime.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the columns to convert.
    columns : list
        List of column names to convert to datetime types.
    format : str, optional
        The strftime to parse dates. If None, it will attempt to infer the format.

    Returns
    -------
    pd.DataFrame
        DataFrame with specified columns converted to datetime types.

    Raises
    ------
    TypeError
        If data is not a DataFrame or columns is not a list.
    ValueError
        If any column specified does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    
    for col in columns:
        data[col] = pd.to_datetime(data[col], format=format)
    return data

# Convert to Categorical
def convert_to_category(data, columns):
    """
    Converts specified columns to categorical types.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the columns to convert.
    columns : list
        List of column names to convert to categorical types.

    Returns
    -------
    pd.DataFrame
        DataFrame with specified columns converted to categorical types.

    Raises
    ------
    TypeError
        If data is not a DataFrame or columns is not a list.
    ValueError
        If any column specified does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    
    for col in columns:
        data[col] = data[col].astype('category')
    return data

# Detect Data Types
def detect_data_types(data):
    """
    Detects and returns data types of columns.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame from which to detect data types.

    Returns
    -------
    pd.Series
        A Series with column names as index and data types as values.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    return data.dtypes

# Change Data Type
def change_dtype(data, column, new_type):
    """
    Changes the data type of a specified column.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the column to change data type.
    column : str
        The name of the column to change.
    new_type : type
        The new data type to convert the column to.

    Returns
    -------
    pd.DataFrame
        DataFrame with the specified column's data type changed.

    Raises
    ------
    TypeError
        If data is not a DataFrame, column is not a string, or new_type is not a valid type.
    ValueError
        If the specified column does not exist in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column, str):
        raise TypeError("Column parameter must be a string.")
    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    if not isinstance(new_type, type):
        raise TypeError("New type must be a valid data type.")
    
    data[column] = data[column].astype(new_type)
    return data

# Convert to Specified Data Types
def correct_data_types(df, column_types):
    """
    Converts columns to specified data types.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    column_types : dict
        Dictionary with column names as keys and data types as values.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns converted to specified data types.

    Raises
    ------
    TypeError
        If df is not a DataFrame or column_types is not a dictionary.
    ValueError
        If any column specified does not exist in the DataFrame or data type is invalid.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column_types, dict):
        raise TypeError("Column types must be provided as a dictionary.")
    for column, dtype in column_types.items():
        if column not in df.columns:
            raise ValueError(f"Column '{column}' is not in the DataFrame.")
        if not isinstance(dtype, type):
            raise TypeError(f"Data type for column '{column}' must be a valid type.")
    
    return df.astype(column_types)