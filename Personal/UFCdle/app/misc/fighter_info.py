import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
fighter_data = []
csv_file = 'Personal/UFCdle/fighter_data.csv'

# Function to convert the date format
def convert_date(date_str):
    try:
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, '%b. %d, %Y')
        # Return the date in the format YYYY-MM-DD
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return None

def store_fighter_data(textfile):
    response = requests.get(f'https://www.ufc.com{textfile}')
    if response.status_code == 200:
        fname = {}

        soup = BeautifulSoup(response.text, 'html.parser')

        #Get Name
        scrape_name = soup.find("h1", class_="hero-profile__name")
        fname['Name'] = scrape_name.text

        if soup.find("p", class_="hero-profile__nickname"):
            scrape_nickname = soup.find("p", class_="hero-profile__nickname")
            fname['Nickname'] = scrape_nickname.text.strip('"')
        else:
            fname['Nickname'] = None
        
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
        scrape_country = soup.find_all("div", class_= "c-bio__field c-bio__field--border-bottom-small-screens")
        for elem in scrape_country:
            if elem.find("div", class_= "c-bio__label").text == 'Hometown':
                hometown = elem.text.strip()
                break
            else:
                hometown = 'Unknown'

    
        if ',' in hometown:
            fname['Country'] = hometown.strip('"').split(', ')[-1]
        else:
            fname['Country'] = hometown.split('\n')[-1]


        # Scrape Rank
        scrape_rank = soup.find("div", class_= "hero-profile__tags")
        rank = ''
        for s in scrape_rank.p.text:
            if s.isdigit():
                rank += s

        if rank != '':
            fname['Rank'] = rank
        else:
            fname['Rank'] = 'C'

        #Scrape debut
        scrape_debut = soup.find_all("div", class_="c-bio__field")
        for elem in scrape_debut:
            if elem.text.find('Octagon') == True:
                debut = elem.text
                break
            else:
                debut = 'Unknown'

        fname['Debut'] = convert_date(debut.strip().split('\n')[-1])
        
        fighter_data.append(fname)

def write_to_csv(fighter_list):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Nickname', 'Division', 'Rank', 'Fighting Style', 'Country', 'Debut'])
        writer.writeheader()
        for fighter in fighter_list:
            writer.writerow(fighter)

# Read and process each line from the text file
with open('Personal/UFCdle/fighter.txt') as f:
    for line in f:
        store_fighter_data(line.strip())

# Write all collected data to CSV
write_to_csv(fighter_data)
