from main import get_link
import requests
from bs4 import BeautifulSoup
import csv

fighter_data = {}
style_options = ['Jiu-Jitsu', 'Wrestler', 'Kickboxer', 'Sambo', 'MMA', 'Boxing', 'Freestyle', 'Grappler']
csv_file = 'fighter_data.csv'

def store_fighter_data():
    response = requests.get(f'https://www.ufc.com/{get_link()}')
    if response.status_code == 200:
        # Parse the UFC fighter content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape Division
        scrape_division = soup.find_all("div", class_="hero-profile__division")
        hero_profile = scrape_division[0].text.split("\n")
        division = hero_profile[1].split(' ')
        for x, item in enumerate(division):
                if item == 'Division':
                        del division[x]         
        dprocessing = ' '.join(map(str, division))    
        fighter_data['Division'] = dprocessing.strip("'[],") 

        # Scrape Fighting Style
        scrape_style = soup.find_all("div", class_="c-bio__text")
        for style in scrape_style:
            if style.text.strip() in style_options:
                fighter_data['Fighting Style'] = style.text.strip()
                break
        else:
            fighter_data['Fighting Style'] = 'MMA'
        print("Fighting Style:", fighter_data['Fighting Style'])  # Debugging statement

        # Scrape Country
        if len(scrape_style) > 1:
            home_town = scrape_style[1].text.strip()
            if ',' in home_town:
                fighter_data['Country'] = home_town.split(', ')[-1]
            else:
                fighter_data['Country'] = home_town
        else:
            fighter_data['Country'] = 'Unknown'
        print("Country:", fighter_data['Country'])  # Debugging statement

def write_to_csv(fighter_dict):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Division', 'Fighting Style', 'Country'])
        writer.writeheader()
        writer.writerow(fighter_dict)  # Write a single row

store_fighter_data()
write_to_csv(fighter_data)
