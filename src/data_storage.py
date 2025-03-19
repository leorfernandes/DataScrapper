import pandas as pd # Import the pandas library to work with dataframes
import os # Import the os library to work with directories
import datetime # Import the datetime library to work with dates and times
from error_handler import log_error # Import the log_error function from error_handler.py
from config import DIRECTORY # Import the DIRECTORY variable from config.py

def save_to_csv(data):
    try:
        # Convert product data into a DataFrame
        df = pd.DataFrame(data, columns=["Product Name", "Price"])

        # Cleaning the talbe
        df = df.drop_duplicates(subset=["Product Name"]) # Eliminate duplicates
        df = df.dropna(how="all") # Eliminate empty rows

        # Get the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define filename to be saved in the configured directory
        directory = DIRECTORY
        if not os.path.exists(directory):
            os.makedirs(directory) # Create the directory if it doesn't exist
        filename = os.path.join(directory, f"product_prices_{timestamp}.csv") # Filename with timestamp

        # Save the DataFrame
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return True
    
    except Exception as e:
        log_error(f"Unexpected error in scrape_product_data: {type(e).__name__}")
    
    return None