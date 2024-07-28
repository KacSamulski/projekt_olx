import requests
from bs4 import BeautifulSoup
import csv

link = 'https://www.olx.pl/elektronika/q-macbook-air-M1/?search%5Bfilter_enum_processorseries_laptops%5D%5B0%5D=apple-m&search%5Bfilter_enum_state%5D%5B0%5D=used&view=list'

page_to_scrape = requests.get(link)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

hrefs = soup.findAll("a", attrs={"class":"css-z3gu2d"})
print(hrefs)
file = open("scrapped_refs.csv", "w")
writer = csv.writer(file)

writer.writerow(["HREFS"])

for href in hrefs:
    writer.writerow([hrefs.text])
file.close