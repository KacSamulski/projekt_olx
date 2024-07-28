import requests
from bs4 import BeautifulSoup
import csv

# URL strony do scrappowania
link = 'https://www.olx.pl/elektronika/q-macbook-air-M1/?search%5Bfilter_enum_processorseries_laptops%5D%5B0%5D=apple-m&search%5Bfilter_enum_state%5D%5B0%5D=used&view=grid'

# Pobierz stronę
page_to_scrape = requests.get(link)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Znajdź wszystkie elementy <a> z klasą css-z3gu2d
hrefs = soup.findAll("a", attrs={"class": "css-z3gu2d"})

# Zapisz wyniki do pliku CSV
with open("scrapped_hrefs.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["HREFS"])  # Nagłówek kolumny

    # Wyodrębnij i zapisz każdy href
    for href in hrefs:
        # Pobierz atrybut href, jeśli istnieje
        url = href.get('href')
        if url:
            writer.writerow([url])

print("Scraping completed and saved to scrapped_hrefs.csv")
