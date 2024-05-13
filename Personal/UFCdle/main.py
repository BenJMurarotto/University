import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get('https://www.ufc.com/rankings')

# Check if the request was successful
if response.status_code == 200:
    # Parse the UFC fighter content
    soup = BeautifulSoup(response.text, 'html.parser')
    fighter_list = []
    # The HTML structure separates champs and ranked fighters, this soup structure retrieves current champ names
    scrape_champs = soup.find_all("div", class_="info")
    for fighter in scrape_champs:
        if fighter.a.text not in fighter_list:
            fighter_list.append(fighter.a.text)
    
    scrape_fighters = soup.find_all("td", class_="views-field views-field-title") 
    print(scrape_fighters)
  
        
    
        
            
        
    


