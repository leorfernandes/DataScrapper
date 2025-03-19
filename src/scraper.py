# Description: This file contains the main function that scrapes the product data from the Amazon website.
from selenium import webdriver # Import the webdriver module from the selenium library
from selenium.webdriver.common.by import By # Import the By class from the selenium library

from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException # Import the exceptions from the selenium library
from selenium.webdriver.support.ui import WebDriverWait # Import the WebDriverWait class from the selenium library
from selenium.webdriver.support import expected_conditions as EC # Import the expected_conditions module from the selenium library

from error_handler import log_error # Import the log_error function from error_handler.py
from config import URL, TIMEOUT, SELECTORS # Import the URL, TIMEOUT, and SELECTORS variables from config.py
from driver_config import get_driver # Import the get_driver function from driver_config.py

def scrape_product_data():
    # Opens the URL and returns the requested elements
    # Handles common errors and logs them
    try:
        # Load driver
        driver = get_driver()

        # Set wait time
        wait = WebDriverWait(driver, TIMEOUT)

        # Navigate to Webpage
        driver.get(URL)
        driver.set_page_load_timeout(TIMEOUT)

        # Access ratings hidden
        driver.execute_script("document.querySelectorAll('.a-icon-star-small').forEach(function(e) { e.removeAttribute('aria-hidden'); })")

        # Extract products details
        titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, SELECTORS["title"]))) # Product Names
        price_whole = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, SELECTORS["price_whole"]))) # Prices
        price_cents = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, SELECTORS["price_cents"])))

        # Create a list to store the data
        product_data = []

        # Loop through the product listings and store the data
        for i in range(len(titles)):
            title = titles[i].text
            price = f"{price_whole[i].text}.{price_cents[i].text}" if i < len(price_whole) and i < len(price_cents) else "N/A"
            product_data.append([title, price])

        # Close the driver
        driver.quit()

        # Return fetched data
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
        
print(scrape_product_data()) # Test the function