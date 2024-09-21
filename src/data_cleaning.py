import pandas as pd
import re


def clean_and_standardize_data(df: pd.DataFrame, requested_variables: list) -> pd.DataFrame:
    """
    Cleans and standardizes the table's data and attempts to match the requested variables
    and their associated values (both headers and data rows).

    Args:
        df (pd.DataFrame): The DataFrame to clean.
        requested_variables (list): List of user-requested variables.

    Returns:
        pd.DataFrame: A DataFrame containing the matched variables and their associated values.
    """
    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Drop empty rows/columns
    df.dropna(how='all', axis=1, inplace=True)
    df.dropna(how='all', axis=0, inplace=True)

    # Result DataFrame to store matched variables and values
    result = pd.DataFrame()

    # For each variable, find its associated value (whether it's a column or row match)
    for var in requested_variables:
        var_pattern = re.compile(re.escape(var), re.IGNORECASE)

        # Check if the variable is found in the column headers
        matched_columns = [col for col in df.columns if var_pattern.search(col)]

        if matched_columns:
            # Extract the numerical data from matched columns
            result[var] = df[
                matched_columns].squeeze()  # Squeeze to convert from DataFrame to Series if it's a single column
        else:
            # If the variable is not in the columns, look for it in the rows (row-wise search)
            for i, row in df.iterrows():
                if any(var_pattern.search(str(cell)) for cell in row):
                    # If a match is found in the row, store the numeric values for that row
                    result[var] = row  # Add the entire row as a match for the variable
                    break  # Break after finding the first match

        # If no match is found, fill NaN for that variable
        if var not in result.columns:
            result[var] = pd.NA

    return result
