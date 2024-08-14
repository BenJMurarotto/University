from app import app
from flask import request, jsonify, render_template, session
import sqlite3

app.secret_key = 'your_secret_key_here'

def connect_db():
    return sqlite3.connect('app/misc/ufcdle.db')

@app.route('/')
@app.route('/index')
def index():
    session.clear()  # Clear session to start fresh
    session['guessed_fighters'] = []
    session['max_guesses'] = 6

    # Select a random secret fighter
    con = connect_db()
    cur = con.cursor()
    cur.execute('SELECT fname, lname FROM fighters ORDER BY RANDOM() LIMIT 1')
    secret_fighter = cur.fetchone()
    con.close()

    session['secret_fighter'] = {'fname': secret_fighter[0], 'lname': secret_fighter[1]}

    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    con = connect_db()
    cur = con.cursor()

    # Ensure the query is case-insensitive and correctly filters fighters
    cur.execute(
        '''SELECT fname, lname FROM fighters WHERE LOWER(fname) LIKE LOWER(?) OR LOWER(lname) LIKE LOWER(?)''', 
        (query.lower() + '%', query.lower() + '%')
    )
    results = cur.fetchall()

    con.close()
    
    if results:
        # Return an array of matching fighters
        return jsonify([{'fname': result[0], 'lname': result[1]} for result in results])
    else:
        return jsonify({'status': 'error', 'message': 'No matching fighter found.'})
