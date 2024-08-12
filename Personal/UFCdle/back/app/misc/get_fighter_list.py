import requests
from bs4 import BeautifulSoup

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
        print(fighter_list)

        
        #scrape_fighters = soup.find_all("td", class_="views-field views-field-title") 
        #for fighter in scrape_fighters:
            #if fighter.a['href'] not in fighter_list:
                #fighter_list.append(fighter.a['href'])

        # Open the file in write mode
        #with open('fighter.txt', mode='w', newline='') as file:
            #for link in fighter_list:
                #file.write(link + '\n')  # Write each link on a new line
    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Call the function to get the links and save them to the file
get_link()
