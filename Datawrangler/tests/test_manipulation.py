def drop_missing_data(df, columns=None):
    """Drop rows with missing data in specified columns."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if columns and not all(col in df.columns for col in columns):
        raise ValueError("Some columns specified are not in the DataFrame.")
    if columns:
        return df.dropna(subset=columns)
    return df.dropna()