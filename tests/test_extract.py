# tests/test_extract.py

import unittest
from src.extract import extract_tables_from_pdf

class TestPDFExtraction(unittest.TestCase):

    def test_extraction(self):
        # Path to a sample PDF that you will use for testing
        pdf_file = 'sample_financial_statement.pdf'

        # Perform table extraction
        tables = extract_tables_from_pdf(pdf_file)

        # Assert that tables are extracted
        self.assertTrue(len(ttables) > 0, "No tables extracted from PDF")

if __name__ == '__main__':
    unittest.main()
