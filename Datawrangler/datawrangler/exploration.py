import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def describe_data(df):
    """
    Provides descriptive statistics for the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    pd.DataFrame
        Descriptive statistics of the DataFrame.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    return df.describe()

def plot_histogram(df, column, bins=10):
    """
    Plots a histogram for a specified column.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    column : str
        Column name to plot.
    bins : int
        Number of bins for the histogram.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If df is not a DataFrame or column is not a string.
    ValueError
        If the specified column does not exist in the DataFrame or is not numeric.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(column, str):
        raise TypeError("Column parameter must be a string.")
    if column not in df.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' must be numeric to plot a histogram.")
    
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(df, col1, col2):
    """
    Plots a scatter plot for two specified columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    col1 : str
        Column name for x-axis.
    col2 : str
        Column name for y-axis.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If df is not a DataFrame or col1/col2 are not strings.
    ValueError
        If the specified columns do not exist in the DataFrame or are not numeric.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if not isinstance(col1, str) or not isinstance(col2, str):
        raise TypeError("Column parameters must be strings.")
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns '{col1}' and/or '{col2}' are not in the DataFrame.")
    if not (pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2])):
        raise ValueError(f"Both columns '{col1}' and '{col2}' must be numeric to plot a scatter plot.")
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df[col1], y=df[col2])
    plt.title(f'Scatter Plot of {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

# Check Data Integrity
def check_data_integrity(data):
    """
    Checks for consistency and integrity of the data.

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    dict
        Dictionary containing information about missing values, duplicates, and outliers.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    integrity_report = {
        'missing_values': data.isnull().sum(),
        'duplicates': data.duplicated().sum(),
        'outliers': {}  # Placeholder for outlier detection function
    }
    # Assuming detect_outliers is defined elsewhere and correctly imported
    try:
        integrity_report['outliers'] = {col: detect_outliers(data, columns=[col])[col] for col in data.select_dtypes(include=np.number).columns}
    except NameError:
        integrity_report['outliers'] = "Outlier detection function is not defined."
    
    return integrity_report

# Data Quality Reports
def data_quality_report(data):
    """
    Generates a data quality report summarizing missing values, duplicates, and outliers.

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    dict
        Dictionary containing summaries of missing values, duplicates, and outliers.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    report = {
        'missing_values_summary': data.isnull().sum(),
        'duplicates_summary': data.duplicated().sum(),
        'outliers_summary': {}  # Placeholder for outlier detection function
    }
    # Assuming detect_outliers and identify_missing are defined elsewhere and correctly imported
    try:
        report['outliers_summary'] = detect_outliers(data)
    except NameError:
        report['outliers_summary'] = "Outlier detection function is not defined."
    
    return report