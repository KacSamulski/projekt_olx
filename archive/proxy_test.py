import requests
from bs4 import BeautifulSoup
import os
import sys
import json

#url = "https://www.scrapingcourse.com/ecommerce/"
url = "https://www.olx.pl/"
response_olx = requests.get(url)
content = response_olx.content
api_link = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country=hr,gi,fi,ee,si,cy,mt,pt,mv,ie,dk,il,lt,at,am,gr,kz,no,al,md,ge,sk,be,ro,me,cz,bg,it,ch,hu,gb,rs,tr,pl,es,ua,fr,de,nl&protocol=http&proxy_format=ipport&format=json&anonymity=Elite&timeout=20000'
#with open("http_proxies_txt", "r", newline='', encoding='utf-8') as file:
response_api_link = requests.get(api_link)
if response_api_link.status_code == 200:
    print("pomyślnie pobrano dane")
    data_api_link_text = response_api_link.text


# Define the paths to the input and output files
#input_file = 'http_proxies.txt'
output_file = 'http_proxies.json'

# Read the contents of the input file
#with open(input_file, 'r') as file:
#    content = file.read()

# Parse the content as JSON
data = json.loads(data_api_link_text)

# Write the parsed data to the output file with indentation
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Plik API został zamieniony na {output_file}.")

with open(output_file, 'r') as file:
    przestrzen = json.load(file)

proxies = [
    
]


for proxy in data.get('proxies', []):
    protocol = proxy.get('protocol')
    ip = proxy.get('ip')
    port = proxy.get('port')
    country = proxy.get('ip_data', {}).get('country')
    proxies.append(f"{protocol}://{ip}:{port}")
    #print(proxies)
    #print(f"IP: {ip}, Port: {port}, Country: {country}")
    #print(f"https://{ip}:{port}")

for proxy in proxies:
    try:
        # make a GET request to the specified URL using the current proxy
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        
        # extract the IP address from the response content
            #ip_address = response.text
        if response.status_code == 200:
            #print(response.text)
        # print the obtained IP address
            print("strona zaladowana poprawnie")
        else:
            proxies.remove(proxy)
    except requests.exceptions.RequestException as e:
        #print(f"Request failed with proxy {proxy}: {str(e)}")
        continue  # move to the next proxy if the request fails






#def loadRatesFromFile(self):
#    if os.path.exists(RATES_FILE):
#        with open(RATES_FILE, 'r') as file:
#            self.rates = json.load(file)
#        QMessageBox.information(self, "Informacja", "Brak połączenia z internetem, załadowano zapisane kursy walut.")
#    else:
#        QMessageBox.critical(self, "Błąd", "Brak połączenia z Internetem i brak zapisanych kursów walut.")
#        sys.exit()