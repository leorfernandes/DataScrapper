import logging
import os
from config import LOG_DIRECTORY

# Ensuure the log directory exists
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

# Configure logging
log_file_path = os.path.join(LOG_DIRECTORY, "scraper_errors.log")
logging.basicConfig(level=logging.ERROR, filename=log_file_path, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

# Handles the error
def log_error(error_message):
    print(f"\n{error_message}") # Print to console
    logging.error(error_message) # Log to file