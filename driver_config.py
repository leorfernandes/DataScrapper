# driver_config

import random
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# User-Agents from https://www.useragentstring.com/pages/Chrome/
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
]

def get_driver():
    options = Options() # Define options function
    user_agent = random.choice(USER_AGENTS) # Select a random User-Agent
    options.add_argument(f"user-agent={user_agent}") # Apply User-Agent
    options.add_argument("--headless") # Run without UI for optimization 

    service = Service(ChromeDriverManager().install()) # Define service
    driver = webdriver.Chrome(service=service, options=options) # Define driver

    return driver

