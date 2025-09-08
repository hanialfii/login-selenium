# login web using selenium
This project is a simple web scraping automation built with selenium and beautifulSoup it logs into the SauceDemo Website, scrapes product data (title, description, and price), and stores the results in a CSV file.

The purpose of this project is to demonstrate how to:
•	Automate login with Selenium.
•	Parse structured data from a webpage using BeautifulSoup.
•	Store scraped data into a CSV file for later analysis.
•	Implement a basic search function across the scraped dataset.
## Features
- AUtomated login using Selenium.
- Product data extaction (title, description, price).
- Export result into CSV file for later analysis.
- Implement a basic search function across the scraped dataset.
## How It Works
1. Login
    The script opens Chrome, navigates to SauceDemo, and logs in using test credentials.
2. Scraping
    Once logged in, it fetches all product data including:
	- Product title
	- Product description
	- Product price
3. Save to CSV
    Extracted data is saved to products.csv in a clean tabular format.
4. Search Function
    You can search data by key (e.g., "title") to return a list of all product names.
## Requirements
- python 3.8+
- Google Chrome
- ChromeDriver (must match your Chrome version)
Install dependencies:
```
pip install selenium beautifulSoup4
```
## Run the Project
```
python scraper.py
```
After running, you'll find:
    - Scraped data saved in products.csv.
	- Search results printed in the terminal.
## Skill Demonstrated
•	Web automation & scraping with Selenium & BeautifulSoup.
•	Data processing and exporting results to CSV.
•	Basic search & filtering logic.
•	Code organization for reusability.

