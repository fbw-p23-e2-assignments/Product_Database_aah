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
        print(response)

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

    cursor.execute("""CREATE TABLE if not EXISTS products(
                title TEXT, 
                category TEXT, 
                price INT, 
                description TEXT, 
                date_added TIMESTAMP,
                total_cost INT
    )""")


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

try: 

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    create_products_table(cursor)

    cursor.execute('DELETE from products')
    print('The rows in products are succesfully deleted')

    start = int(input('Enter the start number: '))
    end = int(input('Enter the end number: '))

    for product_id in range(start ,end + 1):
        data = fetch_product_data(product_id)
        if data:
            insert_product_into_db(cursor, data)

    conn.commit()
    conn.close()
    print('Succesfull imported the data')

except ValueError as v:
    print('Enter no decimal numbers: ', v)

except sqlite3.Error as s:
    print('See here the error: ', s)


