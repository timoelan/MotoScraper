from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.facebook.com/marketplace/category/motorcycles"
driver.get(url)

time.sleep(5)

anzeigen = []

items = driver.find_elements(By.CLASS_NAME, "div.x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24")

for item in items:
    try:
        title_element = item.find_element(By.CLASS_NAME, "span.x1lliihq x6ikm8r x10wlt62 x1n2onr6")
        title = title_element.text.strip() if title_element else "Kein Titel"

        price_element = item.find_element(By.CLASS_NAME, "span.x1lliihq x6ikm8r x10wlt62 x1n2onr6")
        price = price_element.text.strip() if price_element else "Kein Preis"

        anzeigen.append({
            "Titel": title,
            "Preis": price,
        })
    except Exception as e:
        print(f"Fehler: {str(e)}")

driver.quit()

with open("facebook_marketplace.json", "w", encoding="utf-8") as f:
    json.dump(anzeigen, f, ensure_ascii=False, indent=4)

print(f"Gespeicherte Anzeigen: {len(anzeigen)}")
