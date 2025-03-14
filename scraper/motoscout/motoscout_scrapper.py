import requests
from bs4 import BeautifulSoup
import json
import time

base_url = 'https://www.motoscout24.ch/de/s?bodyTypes%5B0%5D=off-road-bike&bodyTypes%5B1%5D=supermoto&pagination%5Bpage={}'

anzeigen = []
page = 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

session = requests.Session()

while True:
    try:
        url = base_url.format(page)
        response = session.get(url, headers=headers)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = soup.find_all('li', class_='css-0') 
        
        if not items:
            print(f"Keine Anzeigen auf Seite {page}. Beende.")
            break

        for item in items:
            try:
                title_tag = item.find('h2', class_='css-svmyrf')
                title = title_tag.text.strip() if title_tag else None
                
                
                price_tag = item.find('p', class_='css-bwl0or')
                price = price_tag.text.strip() if price_tag else None
                
                link_tag = item.find('a')
                link = 'https://www.motoscout24.ch' + link_tag['href'] if link_tag and 'href' in link_tag.attrs else None
                
                img = item.find('img')
                image_url = img['src'] if img and 'src' in img.attrs else None
                
                broken_Inserats = 0

                if not title or not link or not image_url:
                    broken_Inserats + 1
                    continue
                details = {}
                detail_tags = item.find_all('span', class_='css-1kcev50') 
                for detail in detail_tags:
                    text = detail.text.strip()
                    if 'km' in text:
                        details['Kilometerstand'] = text
                    elif 'PS' in text:
                        details['PS'] = text
                    elif 'kW' in text:
                        details['kW'] = text
                
                anzeigen.append({
                    'Titel': title,
                    'Preis': price,
                    'KW': details.get('kW'),
                    'PS': details.get('PS'),
                    'Kilometerstand': details.get('Kilometerstand'),
                    'Link': link,
                    'Bild': image_url,
                    
                })
                
            except Exception as e:
                print(f"Fehler bei Anzeige: {str(e)}")
                continue

        print(f"Seite {page} erfolgreich - {len(items)} Anzeigen")
        print(broken_Inserats)
        page += 1
        
        if page > 10: 
            break

        time.sleep(1) 

    except requests.exceptions.RequestException as e:
        print(f"Fehler bei Seite {page}: {str(e)}")
        break

with open('motoscout24.json', 'w', encoding='utf-8') as f:
    json.dump(anzeigen, f, ensure_ascii=False, indent=4)

print(f"Gespeicherte Anzeigen: {len(anzeigen)}")