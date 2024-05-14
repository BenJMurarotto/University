from main import get_link
import requests
from bs4 import BeautifulSoup
import random

fighter_data = {}

response = requests.get(f'https://www.ufc.com/{get_link()}')
if response.status_code == 200:
        # Parse the UFC fighter content
        soup = BeautifulSoup(response.text, 'html.parser')
        scrape_division = soup.find_all("div", class_="hero-profile__division")
        hero_profile = scrape_division[0].text.split("\n")
        division = hero_profile[1].split(' ')
        if len(division) > 2:
                division.pop(len(division))
                
                        


print(fighter_data)
        
