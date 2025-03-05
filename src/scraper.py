# Import Selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import Error handling
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Imported variables and functions from files
from error_handler import log_error
from config import URL
from driver_config import get_driver

def scrape_product_data():
    # Opens the URL and returns the requested elements
    # Handles common errors and logs them
    try:
        # Load driver
        driver = get_driver()

        # Set wait time
        wait = WebDriverWait(driver, 10)

        # Navigate to Webpage
        driver.get(URL)
        driver.set_page_load_timeout(10)

        # Access ratings hidden
        driver.execute_script("document.querySelectorAll('.a-icon-star-small').forEach(function(e) { e.removeAttribute('aria-hidden'); })")

        # Extract products details
        titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-size-base-plus.a-spacing-none.a-color-base.a-text-normal"))) # Product Names
        price_whole = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-price-whole"))) # Prices
        price_cents = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-price-fraction")))
        ratings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-icon-alt"))) # Ratings
       # num_rantings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-icon-alt"))) # Ratings

        # Create a list to store the data
        product_data = []

        # Loop through the product listings and store the data
        for i in range(len(titles)):
            title = titles[i].text
            price = f"{price_whole[i].text}.{price_cents[i].text}" if i < len(price_whole) and i < len(price_cents) else "N/A"
            rating = ratings[i].text if i < len(ratings) else "N/A"
            product_data.append([title, price, rating])

        # Close the driver
        driver.quit()

        # Return fetched data
        print(product_data)
        return product_data
    
    except TimeoutException as e:
        log_error(f"Timeout while loading {URL}: {type(e).__name__}")

    except NoSuchElementException as e:
        log_error(f"Could not find expected elements on {URL}: {type(e).__name__}")

    except WebDriverException as e:
        log_error(f"Selenium WebDriver error: {type(e).__name__}")
    
    except Exception as e:
        log_error(f"Unexpected error in scrape_product_data: {type(e).__name__}")

    return None # Return None if an error occurs
        
scrape_product_data()