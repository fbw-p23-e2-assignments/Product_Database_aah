import random
from datetime import datetime, timedelta
import sqlite3


def insert_product_into_db(cursor, product_data):
    date_added = datetime.now() - timedelta(days=random.randint(0, 365))
    total_cost = product_data['price'] * random.randint(1, 10)
    
    cursor.execute('''
        INSERT INTO products (title, category, price, description, date_added, total_cost)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        product_data['title'],
        product_data['category'],
        product_data['price'],
        product_data['description'],
        date_added,
        total_cost
    ))
    print(f"Product '{product_data['title']}' added to the database.")

