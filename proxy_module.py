import json
import requests 


def api_import_proxy(api_link):
    response = requests.get(api_link)
    if response.status_code == 200:
        data = json.loads(response.text)
        print("Pomyślnie pobrano dane")
        return data
    else:
        print(f"Błąd podczas pobierania listy proxy. Kod błędu: {response.status_code}")

def save_to_json(data, output_file="proxies.json"):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
        print("Dane zapisane w pliku json")

def load_from_json(input_file="proxies.json"):
    with open(input_file, 'r') as file:
        data = json.load(file)
        print("Wczytano dane z pliku json")
        return data
    

def proxy_validator(data, link, number_of_proxies=6):
    proxies_to_check = [

    ]
    valid_proxies = [

    ]
    for proxy in data.get('proxies', []):
        protocol = proxy.get('protocol')
        ip = proxy.get('ip')
        port = proxy.get('port')
        proxies_to_check.append(f"{protocol}://{ip}:{port}")
        while len(valid_proxies) != min(number_of_proxies, len(proxies_to_check)):
            for proxy in proxies_to_check:
                try:
                    response = requests.get(link, proxies={"http": proxy, "https": proxy})
                    if response.status_code == 200:
                        valid_proxies.append(proxy)
                        print("Strona zaladowana poprawnie.")
                    else:
                        print("Błąd proxy.")
                except requests.exceptions.RequestException as e:
                    
                    continue  
        print(valid_proxies)
        return valid_proxies



if __name__ == "__main__":
    link = 'https://www.olx.pl/'
    api_link = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=json&anonymity=Anonymous&timeout=20000'
    data = api_import_proxy(api_link)
    valid = proxy_validator(data, link)
    save_to_json(valid, 'proxies/valid/valid_proxies.json')

