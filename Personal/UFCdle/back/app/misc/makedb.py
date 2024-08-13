import sqlite3
import csv
con = sqlite3.connect("ufcdle.db")
cur = con.cursor()

### Create database file with attributes corresponding to 'fighter_data.csv'
cur.execute('''DROP TABLE IF EXISTS fighters; ''') ### Delete the current table to avoid the code adding extra rows to the existing db
cur.execute(
'''CREATE TABLE fighters(
fname,   
lname,
nickname,
division,
rank,
style,
country,
debut
)'''      ) 

### Import CSV data into database
with open('fighter_data.csv', 'r') as file:
    reader = csv.reader(file) 
    next(reader) ## This command skips header line of CSV
    for row in reader:
        cur.execute( 
        '''
        INSERT INTO fighters (fname, lname, nickname, division, rank, style, country, debut)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

con.commit()
cur.close()
con.close()


