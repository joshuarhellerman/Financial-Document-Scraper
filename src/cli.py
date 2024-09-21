import os
import pandas as pd
from extract import extract_tables_from_pdf
from data_cleaning import clean_and_standardize_data
from export import export_data
from logger import setup_logger

# Initialize logger
logger = setup_logger()

def main():
    try:
        logger.info("Starting the extraction process")

        # Step 1: Get all PDF files in the 'pdfs/' directory
        pdf_dir = 'pdfs'
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

        if not pdf_files:
            logger.error(f"Error: No PDF files found in the '{pdf_dir}' directory.")
            print(f"Error: No PDF files found in the '{pdf_dir}' directory.")
            return

        logger.info(f"Found {len(pdf_files)} PDF files")

        # Step 2: Input variables for extraction
        requested_variables = input("Enter the variables you want to extract, separated by commas: ").split(',')
        requested_variables = [var.strip().lower() for var in requested_variables]

        # DataFrame to hold all extracted data
        extracted_data = pd.DataFrame()

        # Process each PDF
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_dir, pdf_file)
            logger.info(f"Processing {pdf_file}")

            # Step 3: Extract tables from the PDF
            tables = extract_tables_from_pdf(pdf_path)
            logger.info(f"Extracted {len(tables)} tables from {pdf_file}")

            # Step 4: Search for variables in the extracted tables
            for table in tables:
                cleaned_table = clean_and_standardize_data(table, requested_variables)
                extracted_data = pd.concat([extracted_data, cleaned_table], axis=1)

        # Step 5: Fill in missing variables with NaN
        for var in requested_variables:
            if var not in extracted_data.columns:
                extracted_data[var] = pd.NA

        # Step 6: Export the data to CSV
        export_file_name = input("Enter the export file name (without extension): ")
        export_data(extracted_data, file_format='csv', file_name=export_file_name)
        logger.info(f"Data exported successfully to {export_file_name}.csv")

    except Exception as e:
        logger.error(f"Error in extraction process: {e}")
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()
