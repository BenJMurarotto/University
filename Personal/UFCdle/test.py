import requests
from bs4 import BeautifulSoup
import csv

fighter_data = []
csv_file = 'Personal/UFCdle/fighter_data.csv'

def store_fighter_data(textfile):
    response = requests.get(f'https://www.ufc.com{textfile}')
    if response.status_code == 200:
        fname = {}

        soup = BeautifulSoup(response.text, 'html.parser')
        # Scrape Fighting Style
        scrape_style = soup.find_all("div", class_="c-bio__field c-bio__field--border-bottom-small-screens")
        fighting_style = 'MMA'  # Default value if not found
        
        for elem in scrape_style:
            label = elem.find("div", class_="c-bio__label")
            value = elem.find("div", class_="c-bio__text")
            if label and "Fighting style" in label.text:
                fighting_style = value.text.strip()
                break
        
        fname['Fighting Style'] = fighting_style
        fighter_data.append(fname)

        print(scrape_style)

store_fighter_data('/athlete/israel-adesanya')
print(fighter_data)
