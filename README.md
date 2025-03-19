# Data Scrapper

## Overview
This project is a web scraper that collects product data from a specified URL, saves the data to a CSV file, and provides visualizations and alerts based on the data.

## Features
- Scrapes product titles, prices, and ratings
- Saves data to a CSV file
- Visualizes price trends
- Sends alerts for price drops

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/DataScrapper.git
   cd DataScrapper

2. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

3. Install dependencies:
    pip install -r requirements.txt

## Usage
1. Configure the config.py file with the target URL and other settings.
2. Run the scraper:
    python src/main.py

## Testing
1. Run the unit tests:
    pytest tests/

## License
This project is licensed under the MIT License

