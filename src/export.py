import pandas as pd

def export_data(extracted_data: pd.DataFrame, file_format: str = 'csv', file_name: str = 'extracted_data') -> None:
    """
    Exports the extracted data in the specified format.

    Args:
        extracted_data (pd.DataFrame): The data to export.
        file_format (str): The export format ('csv' or 'excel').
        file_name (str): The name of the output file (without extension).

    Raises:
        ValueError: If the file format is unsupported.
    """
    try:
        if file_format == 'csv':
            extracted_data.to_csv(f'{file_name}.csv', index=False)
        else:
            raise ValueError(f"Unsupported format: {file_format}")
    except Exception as e:
        raise RuntimeError(f"Error exporting data: {e}")
