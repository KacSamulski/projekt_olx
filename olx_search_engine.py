import requests
from bs4 import BeautifulSoup
import proxy_module
import json

things_to_search = {
    'iphone_12_64GB' : 'https://www.olx.pl/oferty/q-iphone-12/?search%5Border%5D=filter_float_price:desc&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=64gb',
    'iphone_12_128GB' : 'https://www.olx.pl/oferty/q-iphone-12/?search%5Border%5D=filter_float_price:desc&search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=128gb&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12&search%5Bfilter_enum_state%5D%5B0%5D=used',
    'iphone_13_128GB' : 'https://www.olx.pl/oferty/q-iphone-13/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=128gb',
    'ipad_air_M1' : 'https://www.olx.pl/elektronika/komputery/tablety/q-ipad-air-M1/?search%5Bfilter_enum_state%5D%5B0%5D=used',
    'playstation_5' : 'https://www.olx.pl/elektronika/gry-konsole/konsole/q-Playstation-5/?search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_version%5D%5B0%5D=playstation5',
    'macbook_air_M1' : 'https://www.olx.pl/elektronika/komputery/laptopy/q-macbook-air-M1/?search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_processorseries_laptops%5D%5B0%5D=apple-m'
}

link = 'https://www.olx.pl/elektronika/komputery/laptopy/q-macbook-air-M1/?search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_processorseries_laptops%5D%5B0%5D=apple-m&search%5Bfilter_enum_disksize_laptops%5D%5B0%5D=129gb-256gb'
api_link = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=json&anonymity=Anonymous&timeout=20000'
proxies_to_check = proxy_module.api_import_proxy(api_link)
proxies_ready = proxy_module.proxy_validator(proxies_to_check, link)
page_to_scrape = requests.get(link, proxies=proxies_ready)
soup = BeautifulSoup(page_to_scrape, "html.parser")


def link_appender(link, my_proxies=proxies_ready):
    links = [
        link
    ]
    counter = 0
    current_page = 1

    try:
        response = requests.get(url, proxies= my_proxies[counter])
        soup = BeautifulSoup(response, 'html.parser')
    
        number_of_pages_string = soup.findAll("a", attrs={"class":"css-1mi714g"})
        number_of_pages = int(number_of_pages_string)
        
        chunk = soup.find4All("a", attrs={"data-testid":"pagination-forward", "data-cy":"pagination-forward"})
        next_page_href = chunk.get("href")
        links.append(next_page_href)
        print(f'number of pages is {number_of_pages}, ilosc linkow to {len(links)}')
    except:
        print("Failed to load initial site")
    finally:
        counter += 1
        current_page += 1
    print(f"obecne proxy {my_proxies[counter]}")
    print(f"obecna strona {current_page}")
    
    while current_page != number_of_pages:
        try:
            res = requests.get(links[current_page], proxies=my_proxies[counter]) 
            soup = BeautifulSoup(response, 'html.parser')
            chunk = soup.find4All("a", attrs={"data-testid":"pagination-forward", "data-cy":"pagination-forward"})
            next_page_href = chunk.get("href")
            links.append(next_page_href)
        except:
            print(f"Nie udalo siena stronie {current_page}")
        finally:
            counter += 1
            current_page += 1
            print(f"obecne proxy {my_proxies[counter]}")
            print(f"obecna strona {current_page}")
        break
    return links

print(link_appender(link))