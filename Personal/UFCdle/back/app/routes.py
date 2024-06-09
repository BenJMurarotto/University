from flask import Blueprint, render_template, request, jsonify, session
from .db import get_db
from random import randint

bp = Blueprint('main', __name__)

def row_to_dict(row):
    return {k: row[k] for k in row.keys()}

@bp.route('/')
def index():
    db = get_db()
    secret_id = randint(1, 173)
    cur = db.execute("SELECT * FROM ufc_fighters WHERE id = ?", (secret_id,))
    secret_fighter = cur.fetchone()
    if secret_fighter:
        session['secret_fighter'] = row_to_dict(secret_fighter)
        print(f"Secret fighter set: {session['secret_fighter']}")  # Debugging statement
    else:
        print("No secret fighter found")  # Debugging statement
    return render_template('index.html')

@bp.route('/ajax_search', methods=['GET'])
def ajax_search():
    try:
        fighter_name = request.args.get('fightername', '')
        db = get_db()
        cur = db.execute('SELECT fname, lname FROM ufc_fighters WHERE fname LIKE ? OR lname LIKE ?', ('%' + fighter_name + '%', '%' + fighter_name + '%'))
        fighters = cur.fetchall()
        fighters_list = [{'fname': fighter['fname'], 'lname': fighter['lname']} for fighter in fighters]
        return jsonify(fighters_list)
    except Exception as e:
        print(f"Error during ajax_search: {str(e)}")  # Debugging statement
        return jsonify({'error': str(e)}), 500

@bp.route('/guess', methods=['POST'])
def guess():
    try:
        data = request.get_json()
        fighter_name = data['fightername']
        print(f"Received guess for fighter: {fighter_name}")  # Debugging statement
        db = get_db()
        cur = db.execute("SELECT * FROM ufc_fighters WHERE fname || ' ' || lname = ?", (fighter_name,))
        fighter = cur.fetchone()

        secret_fighter = session.get('secret_fighter')  # Safely get secret_fighter from session
        print(f"Session data: {session.items()}")  # Debugging statement
        if not secret_fighter:
            print("Secret fighter not found in session")  # Debugging statement
            return jsonify({'error': 'Secret fighter not found in session'}), 500

        if fighter:
            fighter_dict = row_to_dict(fighter)
            print(f"Fighter found: {fighter_dict}")  # Debugging statement
            return jsonify({'fighter': fighter_dict, 'secret_fighter': secret_fighter})
        else:
            print("Fighter not found")  # Debugging statement
            return jsonify({'error': 'Fighter not found'}), 404
    except Exception as e:
        print(f"Error processing guess: {str(e)}")  # Detailed error logging
        return jsonify({'error': str(e)}), 500
