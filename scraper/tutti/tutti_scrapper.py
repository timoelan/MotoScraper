import requests
from bs4 import BeautifulSoup
import json
import re
import os
import time
from datetime import datetime, timedelta

base_url = 'https://www.tutti.ch/de/q/motorraeder/Ak6lzdXBlcm1vdG-rbW90b3JjeWNsZXOUwMDAwA?sorting=newest&page={}&query=supermoto'
json_file = 'tutti_anzeigen.json'

def scrape_new_ads():
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            anzeigen = json.load(f)
    else:
        anzeigen = []

    id_counter = max([anzeige['id'] for anzeige in anzeigen]) + 1 if anzeigen else 1

    page = 1
    new_ads = []

    while True:
        url = base_url.format(page)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Fehler beim Abrufen von {url}: {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', attrs={'data-private-srp-listing-item-id': True})
        
        if not items:
            print(f"Keine weiteren Anzeigen gefunden. Beende bei Seite {page}.")
            break

        for item in items:
            title_tag = item.find('div', class_='MuiBox-root mui-style-1haxbqe')
            title = title_tag.text.strip() if title_tag else 'Kein Titel gefunden'

            link_tag = item.find('a')
            link = 'https://www.tutti.ch' + link_tag['href'] if link_tag else 'Kein Link gefunden'

            description_tag = item.find('div', class_='MuiBox-root mui-style-wkoz8z')
            description = description_tag.text.strip() if description_tag else 'Keine Beschreibung gefunden'

            price_text = item.text  
            price_pattern = r"(\d{1,3}(?:'\d{3})*\.-)"
            matches = re.findall(price_pattern, price_text)
            price = matches[0] if matches else 'Preis nicht gefunden'

            location_tag = item.find('span', class_='MuiTypography-root MuiTypography-body1 mui-style-1xafick')
            location = location_tag.text.strip() if location_tag else 'Keine Standortinformationen gefunden'

            image_tag = item.find('img')
            image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else 'Keine Bild-URL gefunden'

            existing_anzeige = next((anzeige for anzeige in anzeigen if anzeige['Link'] == link), None)

            if existing_anzeige:
                print(f"Anzeige bereits vorhanden: {title}")
                existing_anzeige['status'] = 'read' 
            else:
                new_ad = {
                    'id': id_counter,  
                    'Titel': title,
                    'Link': link,
                    'Beschreibung': description,
                    'Preis': price,
                    'Ort': location,
                    'Bild-URL': image_url,
                    'status': 'unread',
                    'Hinzugefügt am': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                anzeigen.append(new_ad)
                new_ads.append(new_ad)  
                id_counter += 1  

        print(f"Seite {page} verarbeitet, {len(items)} Anzeigen gefunden.")
        page += 1 

    if new_ads:
        print(f"{len(new_ads)} neue Anzeigen gefunden:")
        for ad in new_ads:
            print(f" - {ad['Titel']} ({ad['Link']})")

    anzeigen = [anzeige for anzeige in anzeigen if datetime.now() - datetime.strptime(anzeige['Hinzugefügt am'], '%Y-%m-%d %H:%M:%S') < timedelta(weeks=4)]

    if anzeigen:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(anzeigen, f, ensure_ascii=False, indent=4)
        print(f"Scraping beendet. {len(anzeigen)} Anzeigen gespeichert in '{json_file}'.")
    else:
        print("Keine Anzeigen gefunden. Datei wird nicht erstellt.")

def monitor_new_ads():
    while True:
        print("Starte Scraping...")
        scrape_new_ads()
        print("Warte auf neue Anzeigen...")
        time.sleep(900)  

if __name__ == "__main__":
    monitor_new_ads()