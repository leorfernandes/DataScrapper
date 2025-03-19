from scraper import scrape_product_data # Import the scrape_product_data function from scraper.py
from data_storage import save_to_csv # Import the save_to_csv function from data_storage.py
from config import URL # Import the URL variable from config.py

# Scrape data & Error handling
print(f"Fetching data from {URL}...")
product_data = scrape_product_data()
if product_data:
    print(f"Successfully scraped the requested data")
else:
    print("It looks like something went wrong. Please check the log files.")

# Save data to CSV & Error Handling
print("Saving your data into a csv file...")
try:
    if save_to_csv(product_data):
        print("Successfully saved the data.")
    else:
        print("It looks like something went wrong. Please check the log files.")
except NameError as e:
        print("You need to scrape some data first.")

# Close the program
print("All done! Have a great day!")