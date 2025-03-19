# URL to scrap data
URL = "http://example.com/products"

# HTML Selectors
SELECTORS = {
    "title": ".a-size-base-plus.a-spacing-none.a-color-base.a-text-normal",
    "price_whole": ".a-price-whole",
    "price_cents": ".a-price-fraction",
}

# Timeout to load the page
TIMEOUT = 10

# Directory to save the CSV file
CSV_FILE_PATH = "../data/product_data.csv"

# Directory to save the log files
LOG_DIRECTORY = "../logs"


