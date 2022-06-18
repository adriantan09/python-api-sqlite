import sqlite3

DATABASE_FILE = "games.db"

# converts sql query response to a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db():
    conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
    conn.row_factory = dict_factory
    return conn

db = connect_db()
cursor = db.cursor()
