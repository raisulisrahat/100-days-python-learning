# Here I am showing Problem Solve Day 10

# Here's a simplified example of a web scraping script using Python, Beautiful Soup, and Requests to scrape quotes from http://quotes.toscrape.com:

import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the page
    quotes = []
    for quote in soup.find_all('span', class_='text'):
        quotes.append(quote.text)

    # Print the scraped quotes
    for i, quote in enumerate(quotes, start=1):
        print(f"Quote {i}: {quote}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
