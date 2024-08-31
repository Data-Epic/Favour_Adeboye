import numpy as np
import pandas as pd

def detect_outliers(data, method='IQR', columns=None):
    """
    Detects outliers using specified method (IQR, Z-score).

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to detect outliers.
    method : str, optional
        The method to use for detecting outliers. Options are 'IQR' or 'Z-score'. Default is 'IQR'.
    columns : list, optional
        List of column names to check for outliers. If None, applies to all numeric columns.

    Returns
    -------
    dict
        Dictionary where keys are column names and values are indices of outlier rows.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame, method is not a string, or columns is not a list.
    ValueError
        If an unsupported method is specified or if any columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(method, str):
        raise TypeError("Method parameter must be a string.")
    if method not in ['IQR', 'Z-score']:
        raise ValueError("Method must be either 'IQR' or 'Z-score'.")
    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("Columns parameter must be a list.")
        if not all(col in data.columns for col in columns):
            raise ValueError("Some columns specified are not in the DataFrame.")
    else:
        columns = data.select_dtypes(include=np.number).columns.tolist()
    
    outliers = {}
    for col in columns:
        if method == 'IQR':
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers[col] = data[(data[col] < Q1 - 1.5 * IQR) | (data[col] > Q3 + 1.5 * IQR)].index
        elif method == 'Z-score':
            mean = data[col].mean()
            std = data[col].std()
            outliers[col] = data[(data[col] > mean + 3 * std) | (data[col] < mean - 3 * std)].index
    return outliers

def remove_outliers(data, method='IQR', columns=None):
    """
    Removes outliers using specified method (IQR, Z-score).

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to remove outliers.
    method : str, optional
        The method to use for detecting outliers. Options are 'IQR' or 'Z-score'. Default is 'IQR'.
    columns : list, optional
        List of column names to remove outliers from. If None, applies to all numeric columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with outliers removed.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame, method is not a string, or columns is not a list.
    ValueError
        If an unsupported method is specified or if any columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    outliers = detect_outliers(data, method, columns)
    for col, indices in outliers.items():
        data.drop(index=indices, inplace=True)
    return data

def cap_outliers(data, method='IQR', columns=None):
    """
    Caps outliers to a specified limit (e.g., 1.5*IQR).

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to cap outliers.
    method : str, optional
        The method to use for detecting outliers. Only 'IQR' is supported. Default is 'IQR'.
    columns : list, optional
        List of column names to cap outliers. If None, applies to all numeric columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with outliers capped.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame, method is not a string, or columns is not a list.
    ValueError
        If method is not 'IQR' or if any columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if method != 'IQR':
        raise ValueError("Only 'IQR' method is supported for capping outliers.")
    
    if columns is None:
        columns = data.select_dtypes(include=np.number).columns.tolist()
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")

    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[col] = np.where(data[col] < lower_bound, lower_bound, data[col])
        data[col] = np.where(data[col] > upper_bound, upper_bound, data[col])
    return data

def replace_outliers(data, method='median', columns=None):
    """
    Replaces outliers with median or mean.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to replace outliers.
    method : str, optional
        The method to use for replacing outliers. Options are 'median' or 'mean'. Default is 'median'.
    columns : list, optional
        List of column names to replace outliers in. If None, applies to all numeric columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with outliers replaced.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame, method is not a string, or columns is not a list.
    ValueError
        If an unsupported method is specified or if any columns are not in the DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(method, str):
        raise TypeError("Method parameter must be a string.")
    if method not in ['median', 'mean']:
        raise ValueError("Method must be either 'median' or 'mean'.")
    
    if columns is None:
        columns = data.select_dtypes(include=np.number).columns.tolist()
    if not isinstance(columns, list):
        raise TypeError("Columns parameter must be a list.")
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    
    for col in columns:
        outliers = detect_outliers(data, 'IQR', [col])[col]
        if method == 'median':
            data.loc[outliers, col] = data[col].median()
        elif method == 'mean':
            data.loc[outliers, col] = data[col].mean()
    return data