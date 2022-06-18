# run this file to reset the database

from db_config import cursor

with open('database/init.sql', 'r') as sql_file:
    script = sql_file.read()
    cursor.executescript(script)
