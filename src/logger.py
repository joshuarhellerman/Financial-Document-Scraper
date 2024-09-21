# src/logger.py

import logging
import os

def setup_logger():
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    logging.basicConfig(
        filename='logs/extraction.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    # Add a console handler for output to the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(console_handler)

    return logger
