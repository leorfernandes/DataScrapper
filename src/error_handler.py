import logging

# Configure file
logging.basicConfig(level=logging.ERROR, filename="scraper_errors.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

# Handles the error
def log_error(error_message):
    print(f"\n{error_message}") # Print to console
    logging.error(error_message) # Log to file