import sqlite3

DATABASE_NAME = "games.db"

# converts sql query response to a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = dict_factory
    return conn

def get_cursor():
    return get_db().cursor()
