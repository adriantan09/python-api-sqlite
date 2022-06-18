DROP TABLE IF EXISTS games;

CREATE TABLE IF NOT EXISTS games(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    publisher TEXT NOT NULL
);

INSERT INTO games (name, price, publisher)
VALUES 
    ('GTA V', '99.9', 'Rockstar Games'),
    ('Red Dead Redemption 2', '76.6', 'Rockstar Games'),
    ('Uncharted 3', '65.2', 'Naughty Dog');
