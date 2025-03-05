import pandas as pd
from datetime import datetime
from error_handler import log_error

def save_to_csv(data):
    try:
        # Convert product data into a DataFrame
        df = pd.DataFrame(data, columns=["Product Name", "Price", "Rating"])

        # Cleaning the talbe
        df = df.drop_duplicates(subset=["Product Name"]) # Eliminate duplicates
        df = df.dropna(how="all") # Eliminate empty rows

        # Get the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define filename to be saved
        filename = f"product_prices_{timestamp}.csv"

        # Save the DataFrame
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return True
    
    except Exception as e:
        log_error(f"Unexpected error in scrape_product_data: {type(e).__name__}")
    
    return None