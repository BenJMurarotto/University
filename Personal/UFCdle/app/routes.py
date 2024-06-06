from flask import Blueprint, render_template, request
from .db import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search', methods=['POST'])
def search():
    fighter_name = request.form['fightername']
    db = get_db()
    cur = db.execute('SELECT fname, lname, nickname, rank, division, style, country, debut FROM ufc_fighters WHERE fname LIKE ? OR lname LIKE ?', ('%' + fighter_name + '%', '%' + fighter_name + '%'))
    fighters = cur.fetchall()
    print(f"Search query: {fighter_name}")
    print(f"Number of fighters found: {len(fighters)}")
    for fighter in fighters:
        print({key: fighter[key] for key in fighter.keys()})  # Ensure correct access
    return render_template('search_results.html', fighters=fighters)
