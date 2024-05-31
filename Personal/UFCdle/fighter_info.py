import requests
from bs4 import BeautifulSoup
import csv

fighter_data = []
style_options = ['Jiu-Jitsu', 'Wrestler', 'Kickboxer', 'Sambo', 'MMA', 'Boxing', 'Freestyle', 'Grappler']
csv_file = 'Personal/UFCdle/fighter_data.csv'

def store_fighter_data(textfile):
    response = requests.get(f'https://www.ufc.com{textfile}')
    if response.status_code == 200:
        fname = {}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape Division
        scrape_division = soup.find_all("div", class_="hero-profile__division")
        if scrape_division:
            scrape_division = soup.find("p", class_="hero-profile__division-title")
            fdivision = scrape_division.text.strip(' Division')
            fname['Division'] = fdivision


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

        # Scrape Country
        scrape_country = soup.find("div", class_= "c-bio__field c-bio__field--border-bottom-small-screens")
        nested_scrape = scrape_country.find("div", class_= "c-bio__text")
        if ',' in nested_scrape.text:
            fname['Country'] = nested_scrape.text.split(', ')[-1]
        else:
            fname['Country'] = nested_scrape.text

        # Scrape Rank
        scrape_rank = soup.find("div", class_= "c-bio__field c-bio__field--border-bottom-small-screens")

        fighter_data.append(fname)

def write_to_csv(fighter_list):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Division', 'Fighting Style', 'Country'])
        writer.writeheader()
        for fighter in fighter_list:
            writer.writerow(fighter)

# Read and process each line from the text file
with open('Personal/UFCdle/fighter.txt') as f:
    for line in f:
        store_fighter_data(line.strip())

# Write all collected data to CSV
write_to_csv(fighter_data)
