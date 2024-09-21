import tabula
import pandas as pd
from typing import List

def extract_tables_from_pdf(pdf_file: str) -> List[pd.DataFrame]:
    """
    Extracts all tables from the provided PDF.

    Args:
        pdf_file (str): The path to the PDF file.

    Returns:
        List[pd.DataFrame]: A list of DataFrames, each representing a table in the PDF.
    """
    try:
        tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
        if not tables:
            raise ValueError("No tables found in the PDF.")
        return tables
    except Exception as e:
        raise RuntimeError(f"Error extracting tables from {pdf_file}: {e}")
