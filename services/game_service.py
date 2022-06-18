from database.db_config import db, cursor

# Helper function
def error(message):
    return { "error": message }

# Service functions
def get_games():
    query = "SELECT * FROM games"
    cursor.execute(query)
    return cursor.fetchall()

def get_game_by_id(id):
    statement = "SELECT * FROM games WHERE id = ?"
    cursor.execute(statement, [id])

    game = cursor.fetchone()
    if game is None:
        return error(f"Unable to locate game with id: {id}")

    return game

def insert_game(body):
    statement = "INSERT INTO games(name, price, publisher) VALUES (?, ?, ?)"
    cursor.execute(statement, [
        body["name"],
        body["price"],
        body["publisher"]
    ])
    db.commit()

    return {}

def update_game(id, body):
    game = get_game_by_id(id)
    if game.get("error"):
        return game

    statement = "UPDATE games SET name = ?, price = ?, publisher = ? WHERE id = ?"
    cursor.execute(statement, [
        body["name"],
        body["price"],
        body["publisher"],
        id
    ])
    db.commit()

    return {}

def delete_game(id):
    game = get_game_by_id(id)
    if game.get("error"):
        return game

    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()

    return {}
