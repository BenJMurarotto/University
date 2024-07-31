import sqlite3
from flask import g, current_app

def get_db():
    if 'db' not in g:
        print(f"Connecting to database at {current_app.config['DATABASE']}")  # Debugging statement
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
