import matplotlib.pyplot as plt
from error_handler import log_error

def plot_price_trends(product_data):
    try:
        visualization = 1
        
        # Convert prices to float for plotting and filter invalid data
        #filtered_data = [
           # (product[0], float(product[1].replace(",","").replace("$", ""))) 
            #for product in product_data 
            #if product[1] and product[1].replace(",", "").replace("$", "").replace(".", "").isdigit()
        #

        # Sort by price (Ascending)
        # sorted_data = sorted(filtered_data, key=lambda x: x[1])

        # Separate names and prices
        #product_names, product_prices = zip(*filtered_data)

        match visualization:
            case 1:
                plt.figure(figsize=(12,6))
                plt.bar(product_data["Product Name"], product_data["Price"])
                plt.xticks(rotation=90)
                plt.title("Price Distribution of Amazon TVs")
                plt.ylabel("Price ($)")
                plt.show()

            case 2:
                plt.scatter(product_data["Product Name"], product_data["Price"])
                plt.xticks(rotation=90)
                plt.title("Price vs Rating Distribution of Amazon TVs")
                plt.ylabel("Price ($)")
                plt.xlabel("Rating")
                plt.show()

            case 3:
                rating_counts = product_data["Rating"]
                plt.pie(product_data["Product Name"], product_data["Price"])
                plt.xticks(rotation=90)
                plt.title("Price vs Rating Distribution of Amazon TVs")
                plt.ylabel("Price ($)")
                plt.xlabel("Rating")
                plt.show()
            
        return True

    except Exception as e:
        log_error(f"Unexpected error in scrape_product_data: {type(e).__name__}")

    return None