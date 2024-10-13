import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

fighter_data = []
csv_file = 'fighter_data.csv'

# Function to convert the date format
def convert_date(date_str):
    try:
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, '%b. %d, %Y')
        # Return the date in the format YYYY-MM-DD
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return None

# Add an auto-incrementing id to each fighter
id_counter = 1

def store_fighter_data(textfile):
    global id_counter
    response = requests.get(f'https://www.ufc.com{textfile}')
    if response.status_code == 200:
        fname = {}
        
        # Assign the current id and increment it
        fname['id'] = id_counter
        id_counter += 1

        soup = BeautifulSoup(response.text, 'html.parser')

        #Get Name
        scrape_name = soup.find("h1", class_="hero-profile__name")
        namesplit = scrape_name.text.split()
        if len(namesplit) > 0:
            fname['fname'] = namesplit[0]

        if len(namesplit) == 1:
            fname['lname'] = ''
        elif len(namesplit) == 2:
            fname['lname'] = namesplit[1]
        elif len(namesplit) > 2:
            fname['lname'] = ' '.join(namesplit[1:])

        if soup.find("p", class_="hero-profile__nickname"):
            scrape_nickname = soup.find("p", class_="hero-profile__nickname")
            fname['nickname'] = scrape_nickname.text.strip('"')
        else:
            fname['nickname'] = None
        
        # Scrape Division
        scrape_division = soup.find_all("div", class_="hero-profile__division")
        if scrape_division:
            scrape_division = soup.find("p", class_="hero-profile__division-title")
            fdivision = scrape_division.text.strip(' Division')
            fname['division'] = fdivision


        # Scrape Fighting Style
        scrape_style = soup.find_all("div", class_="c-bio__field c-bio__field--border-bottom-small-screens")
        fighting_style = 'MMA'  # Default value if not found
        
        for elem in scrape_style:
            label = elem.find("div", class_="c-bio__label")
            value = elem.find("div", class_="c-bio__text")
            if label and "Fighting style" in label.text:
                fighting_style = value.text.strip()
                break
        
        fname['style'] = fighting_style

        # Scrape Country
        scrape_country = soup.find_all("div", class_= "c-bio__field c-bio__field--border-bottom-small-screens")
        for elem in scrape_country:
            if elem.find("div", class_= "c-bio__label").text == 'Hometown':
                hometown = elem.text.strip()
                break
            else:
                hometown = 'Unknown'

        if ',' in hometown:
            fname['country'] = hometown.strip('"').split(', ')[-1]
        else:
            fname['country'] = hometown.split('\n')[-1]

        # Scrape Rank
        scrape_rank = soup.find("div", class_= "hero-profile__tags")
        rank = ''
        for s in scrape_rank.p.text:
            if s.isdigit():
                rank += s

        if rank != '':
            fname['rank'] = rank
        else:
            if len(fighter_data) <= 11:
                fname['rank'] = 'C'
            else:
                # Convert the last rank to an integer, increment it, and convert it back to a string
                last_rank = int(fighter_data[-1]['rank'])
                if last_rank == 15:
                    fname['rank'] = '1'
                else:    
                    fname['rank'] = str(last_rank + 1)

        # Scrape debut
        scrape_debut = soup.find_all("div", class_="c-bio__field")
        for elem in scrape_debut:
            if elem.text.find('Octagon') != -1:
                debut = elem.text
                break
            else:
                debut = 'Unknown'

        fname['debut'] = convert_date(debut.strip().split('\n')[-1])
        
        fighter_data.append(fname)

# Function to write fighter data to CSV
def write_to_csv(fighter_list):
    with open(csv_file, mode='w', newline='') as file:
        # Add 'id' to the list of fieldnames
        writer = csv.DictWriter(file, fieldnames=['id', 'fname', 'lname', 'nickname', 'division', 'rank', 'style', 'country', 'debut'])
        writer.writeheader()
        for fighter in fighter_list:
            writer.writerow(fighter)

# Read and process each line from the text file
def make_csv():
    with open('fighter.txt') as f:
        for line in f:
            store_fighter_data(line.strip())

    # Write all collected data to CSV
    write_to_csv(fighter_data)

make_csv()
