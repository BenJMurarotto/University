from flask import Blueprint, jsonify, request
from .db import get_db

bp = Blueprint('main', __name__)

def row_to_dict(row):
    return {k: row[k] for k in row.keys()}

@bp.route('/ajax_search', methods=['GET'])
def ajax_search():
    try:
        fighter_name = request.args.get('fightername', '')
        db = get_db()
        print(f"Searching for fighter name: {fighter_name}")  # Debugging statement
        cur = db.execute('SELECT fname, lname FROM ufc_fighters WHERE fname LIKE ? OR lname LIKE ?', ('%' + fighter_name + '%', '%' + fighter_name + '%'))
        fighters = cur.fetchall()
        fighters_list = [{'fname': fighter['fname'], 'lname': fighter['lname']} for fighter in fighters]
        return jsonify(fighters_list)
    except Exception as e:
        print(f"Error during ajax_search: {str(e)}")  # Debugging statement
        return jsonify({'error': str(e)}), 500

@bp.route('/fighter_details', methods=['GET'])
def fighter_details():
    try:
        fighter_name = request.args.get('fightername', '')
        db = get_db()
        print(f"Getting details for fighter: {fighter_name}")  # Debugging statement

        names = fighter_name.split()
        if len(names) < 2:
            return jsonify({'error': 'Please enter both first and last name'}), 400

        first_name, last_name = names[0], " ".join(names[1:])
        print(f"First name: {first_name}, Last name: {last_name}")  # Debugging statement

        cur = db.execute('SELECT * FROM ufc_fighters WHERE fname = ? AND lname = ?', (first_name, last_name))
        fighter = cur.fetchone()
        if fighter:
            return jsonify(row_to_dict(fighter))
        else:
            return jsonify({'error': 'Fighter not found'}), 404
    except Exception as e:
        print(f"Error during fighter_details: {str(e)}")  # Debugging statement
        return jsonify({'error': str(e)}), 500
