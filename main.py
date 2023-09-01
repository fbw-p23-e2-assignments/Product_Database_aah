import requests
import sqlite3
from datetime import datetime, timedelta
import random


def fetch_product_data(product_id):
    # Define the API URL with the product ID.
    api_url = f"https://fakestoreapi.com/products/{product_id}"

    try:
        # Send a GET request to the API.
        response = requests.get(api_url)

        # Check if the request was successful (status code 200).
        if response.status_code == 200:
            # Parse the JSON response to get product data.
            product_data = response.json()
            return product_data
        else:
            print(
                f"Failed to fetch data for product ID {product_id}. Status code: {response.status_code}"
            )
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data for product ID {product_id}: {e}")
        return None


def create_products_table(cursor):
    conn = sqlite3.connect()
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE if not EXISTS products(
                title TEXT, 
                category TEXT, 
                price INT, 
                description TEXT, 
                date_added TIMESTAMP
    )"""
    )


def insert_product_into_db(cursor, product_data):
    date_added = datetime.now() - timedelta(days=random.randint(0, 365))
    total_cost = product_data["price"] * random.randint(1, 10)

    cursor.execute(
        """
        INSERT INTO products (title, category, price, description, date_added, total_cost)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (
            product_data["title"],
            product_data["category"],
            product_data["price"],
            product_data["description"],
            date_added,
            total_cost,
        ),
    )
    print(f"Product '{product_data['title']}' added to the database.")
