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

# Opens the URL and returns the requested elements
# Handles common errors and logs them
# Load driver
driver = get_driver()

# Set wait time
wait = WebDriverWait(driver, 10)

# Navigate to Webpage
driver.get(URL)
driver.set_page_load_timeout(10)  
reviews_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-cy="reviews-block"]')))

driver.execute_script("document.querySelectorAll('.a-icon-star-small').forEach(function(e) { e.removeAttribute('aria-hidden'); })")

# Extract products details
titles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-size-base-plus"))) # Product Names
prices = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-price-whole"))) # Prices
ratings = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "a-icon-alt")))
# num_rantings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-icon-alt"))) # Ratings

# Loop through the product listings and store the data
for i in range(len(titles)):
    rating = ratings[i].text if i < len(ratings) else "N/A"
    print(rating)
    
