from db import get_db

def insert_game(name, price, publisher):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(name, price, publisher) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, publisher])
    db.commit()
    return True

def update_game(id, name, price, publisher):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, publisher = ? WHERE id = ?"
    cursor.execute(statement, [name, price, publisher, id])
    db.commit()
    return True

def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_game_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_games():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games"
    cursor.execute(query)
    return cursor.fetchall()
