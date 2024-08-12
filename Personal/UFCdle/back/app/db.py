import sqlite3
from flask import g, current_app

def get_db():
    if 'db' not in g:
        database_path = current_app.config['DATABASE']
        print(f"Connecting to database at {database_path}")  # Debugging statement
        g.db = sqlite3.connect(
            database_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
