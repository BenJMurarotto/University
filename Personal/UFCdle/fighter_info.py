from main import get_link
import requests
from bs4 import BeautifulSoup
import random

fighter_data = {}
style_options = ['Jiu-Jitsu', 'Wrestler', 'Kickboxer', 'Sambo', 'MMA', 'Boxing', 'Freestyle', 'Grappler']

response = requests.get(f'https://www.ufc.com/{get_link()}')
if response.status_code == 200:
        # Parse the UFC fighter content
        soup = BeautifulSoup(response.text, 'html.parser')
        scrape_division = soup.find_all("div", class_="hero-profile__division")
        hero_profile = scrape_division[0].text.split("\n")
        division = hero_profile[1].split(' ')
        for x, item in enumerate(division):
                if item == 'Division':
                        del division[x]         
        dprocessing = ' '.join(map(str, division))    
        fighter_data['Division'] = dprocessing.strip("'[],") 

        scrape_style = soup.find_all("div", class_="c-bio__text")
        for style in scrape_style:
                if style.text in style_options:
                        fighter_data['Fighting Style'] = style
                else: 
                        fighter_data['Fighting Style'] = 'MMA' 
        
        
        print(scrape_style)
        print(len(scrape_style))
        print(fighter_data)

        
        

        

        
