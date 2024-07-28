import requests
from bs4 import BeautifulSoup
import csv

link = 'https://www.olx.pl/d/oferta/macbook-air-m1-8gb-256gb-pokrowiec-guess-magic-mouse-gold-zloty-CID99-ID10cMMq.html'
page_to_scrape = requests.get(link)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.findAll("h4", attrs={"class":"css-1kc83jo"})
prices = soup.findAll("h3", attrs={"class":"css-90xrc0"})

with open("scrapped_name_price.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["NAME","PRICE"])  # Nagłówek kolumny

    # Wyodrębnij i zapisz każdy href
    for name, price in zip(names,prices):
        # Pobierz atrybut href, jeśli istnieje
        writer.writerow([name.text, price.text])
    file.close