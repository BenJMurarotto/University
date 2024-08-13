from app import app
from flask import request, jsonify, render_template
import sqlite3

def connect_db():
    return sqlite3.connect('app/misc/ufcdle.db')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    con = connect_db()
    cur = con.cursor()

    cur.execute(
        '''SELECT fname, lname FROM fighters WHERE fname LIKE ? OR lname LIKE ?''', 
        (query + '%', query + '%')
    )
    results = cur.fetchall()

    con.close()
    return jsonify(results)
