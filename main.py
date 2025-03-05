from scraper import scrape_product_data
from utils import save_to_csv
from visualization import plot_price_trends
from alerts import send_price_alert
from config import URL
from menu import menu

while True:
    match menu():
        case 1: # Scrape data & Error handling
            print(f"Fetching data from {URL}...")
            product_data = scrape_product_data()
            if product_data:
                print(f"Successfully scraped the requested data")
            else:
                print("It looks like something went wrong. Please check the log files.")

        case 2: # Save data to CSV & Error Handling
            print("Saving your data into a csv file...")
            try:
                if save_to_csv(product_data):
                    print("Successfully saved the data.")
                else:
                    print("It looks like something went wrong. Please check the log files.")
            except NameError as e:
                print("You need to scrape some data first.")

        case 0: # Close the program
            print("Closing the program...")
            exit()

# Visualize a graph
#print("Creating a graph...")

#if plot_price_trends(product_data):
    #print("Graph was successfully created.")
#else:
    #print("It looks like something went wrong.")
    #exit()

# Set up alerts if prices drops
#send_price_alert(product_data)