import sqlite3

DATABASE = '/home/adduser/University/Personal/UFCdle/instance/ufcdle.db'

def verify_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Check if the table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ufc_fighters';")
    table_exists = cur.fetchone()

    if table_exists:
        print("Table 'ufc_fighters' exists.")
        cur.execute("SELECT COUNT(*) FROM ufc_fighters;")
        count = cur.fetchone()[0]
        print(f"Number of records in 'ufc_fighters': {count}")
    else:
        print("Table 'ufc_fighters' does not exist.")

    conn.close()

if __name__ == '__main__':
    verify_db()
