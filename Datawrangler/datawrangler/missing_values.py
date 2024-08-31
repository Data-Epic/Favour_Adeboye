import pandas as pd

def identify_missing(data):
    """
    Returns a summary of missing values in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to check for missing values.

    Returns
    -------
    pd.Series
        A series with the count of missing values for each column.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    return data.isnull().sum()

def impute_missing(data, method='mean', columns=None):
    """
    Imputes missing values using the specified method (mean, median, mode, or a constant value).

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to impute missing values in.
    method : str or any, optional
        The method to use for imputation: 'mean', 'median', 'mode', or a constant value. Default is 'mean'.
    columns : list, optional
        List of column names to apply imputation. If None, applies to all columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with missing values imputed.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame or columns is not a list.
    ValueError
        If the specified method is not 'mean', 'median', 'mode', or a constant value.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in data.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
    else:
        columns = data.columns

    valid_methods = ['mean', 'median', 'mode']
    for col in columns:
        if method == 'mean':
            data[col].fillna(data[col].mean(), inplace=True)
        elif method == 'median':
            data[col].fillna(data[col].median(), inplace=True)
        elif method == 'mode':
            data[col].fillna(data[col].mode()[0], inplace=True)
        elif isinstance(method, (int, float, str)):
            data[col].fillna(method, inplace=True)
        else:
            raise ValueError(f"Invalid method '{method}'. Choose from 'mean', 'median', 'mode', or provide a constant value.")
    return data

def fill_forward(data, columns=None):
    """
    Fills missing values using forward fill.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to fill missing values.
    columns : list, optional
        List of column names to apply forward fill. If None, applies to all columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with missing values forward-filled.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame or columns is not a list.
    ValueError
        If any of the specified columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in data.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
        return data.ffill(axis=0)[columns]
    
    return data.ffill(axis=0)

def fill_backward(data, columns=None):
    """
    Fills missing values using backward fill.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to fill missing values.
    columns : list, optional
        List of column names to apply backward fill. If None, applies to all columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with missing values backward-filled.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame or columns is not a list.
    ValueError
        If any of the specified columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in data.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
        return data.bfill(axis=0)[columns]
    
    return data.bfill(axis=0)

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