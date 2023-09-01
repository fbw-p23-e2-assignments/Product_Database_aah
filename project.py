

import requests
import sqlite3
from datetime import datetime

def create_products_table(cursor):
    conn = sqlite3.connect()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE if not EXISTS products(
                title TEXT, 
                category TEXT, 
                price INT, 
                description TEXT, 
                date_added TIMESTAMP
    )""")











