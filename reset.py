# run this file to reset the database

from db import get_cursor

with open('init.sql', 'r') as sql_file:
    script = sql_file.read()
    get_cursor().executescript(script)
