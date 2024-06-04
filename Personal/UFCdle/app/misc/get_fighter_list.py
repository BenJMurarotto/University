import requests
from bs4 import BeautifulSoup
import random

def get_link():
    # Send a GET request to the URL
    response = requests.get('https://www.ufc.com/rankings')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the UFC fighter content
        soup = BeautifulSoup(response.text, 'html.parser')
        fighter_list = []
        # The HTML structure separates champs and ranked fighters, this soup structure retrieves current champ names
        scrape_champs = soup.find_all("div", class_="info")
        for champ in scrape_champs:
            if champ.a['href'] not in fighter_list:
                fighter_list.append(champ.a['href'])
        
        scrape_fighters = soup.find_all("td", class_="views-field views-field-title") 
        for fighter in scrape_fighters:
            if fighter.a['href'] not in fighter_list:
                fighter_list.append(fighter.a['href'])


    count_fighters = len(fighter_list)
    ###select_fighter = random.randint(0, count_fighters) - this segment of code was to pull a random fighter from fighter_list
   ### print(fighter_list[select_fighter])
   ####  return((fighter_list[select_fighter]))
    return fighter_list
    

    


