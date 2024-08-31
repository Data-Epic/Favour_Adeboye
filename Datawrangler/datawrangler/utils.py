import pandas as pd
import os

def load_data(file_path, file_type='csv'):
    """
    Loads data from a file into a DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the data file.
    file_type : str, optional
        Type of file to load ('csv', 'excel'). Default is 'csv'.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.

    Raises
    ------
    FileNotFoundError
        If the file does not exist at the specified path.
    ValueError
        If the specified file type is not supported.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at path {file_path} does not exist.")
    
    if file_type == 'csv':
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise ValueError(f"Failed to read CSV file: {e}")
    elif file_type == 'excel':
        try:
            return pd.read_excel(file_path)
        except Exception as e:
            raise ValueError(f"Failed to read Excel file: {e}")
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'excel'.")

def save_cleaned_data(data, filename, file_format='csv'):
    """
    Exports the cleaned and processed dataset to various formats.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to save.
    filename : str
        The name of the file to save the data.
    file_format : str, optional
        The format to save the data ('csv', 'excel', 'json', 'sql'). Default is 'csv'.

    Raises
    ------
    ValueError
        If the specified file format is not supported.
    Exception
        If there is an issue saving the file.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame.")
    
    try:
        if file_format == 'csv':
            data.to_csv(filename, index=False)
        elif file_format == 'excel':
            data.to_excel(filename, index=False)
        elif file_format == 'json':
            data.to_json(filename, orient='records')
        elif file_format == 'sql':
            import sqlite3
            conn = sqlite3.connect(filename)
            data.to_sql('cleaned_data', conn, index=False, if_exists='replace')
            conn.close()
        else:
            raise ValueError("Invalid file format. Use 'csv', 'excel', 'json', or 'sql'.")
    except Exception as e:
        raise Exception(f"Failed to save data to {file_format} format: {e}")

def log_changes(change_description, log_file='data_wrangling.log'):
    """
    Logs data transformations and cleaning steps for traceability.

    Parameters
    ----------
    change_description : str
        A description of the changes made to the data.
    log_file : str, optional
        The path to the log file. Default is 'data_wrangling.log'.

    Raises
    ------
    IOError
        If the log file cannot be written.
    """
    if not isinstance(change_description, str):
        raise TypeError("Change description must be a string.")
    if not isinstance(log_file, str):
        raise TypeError("Log file path must be a string.")
    
    try:
        with open(log_file, 'a') as log:
            log.write(f"{change_description}\n")
    except IOError as e:
        raise IOError(f"Failed to write to log file {log_file}: {e}")