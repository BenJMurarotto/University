import sqlite3
from flask import g

DATABASE = '/Users/benmurarotto/Desktop/UniNotes/University/Personal/UFCdle/app/misc/ufcdle.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # This will allow us to access rows as dictionaries
    return db

def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
