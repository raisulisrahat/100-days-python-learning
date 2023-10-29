# Here I am showing DavOps Project Day 8

import requests
from bs4 import BeautifulSoup

def scrape_dynamic_content(url):
    all_results = []
    page_number = 1
    while True:
        response = requests.get(f"{url}?page={page_number}")

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', class_='result')

        if not results:
            break

        all_results.extend(results)
        page_number += 1

    return all_results

# Usage
scraped_data = scrape_dynamic_content('https://www.amarstock.com')

# Save the scraped data into a text file
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    for result in scraped_data:
        file.write(result.get_text() + '\n')

