# Exercise: Creating a Product Database

Objective:

Practice working with APIs, SQLite databases, and generating random datetimes by creating a script that fetches product data from an API, generates random datetimes, and stores the information in an SQLite database.

Instructions:

1. *Setup:*
   - Install the requests library if you haven't already: pip install requests
2. *Task:*
   - Write a Python script that fetches product data from the "Fake Store API" using the requests library for a range of product IDs (e.g., from 1 to 10).
   - For each product fetched, generate a random datetime within the past year and store the product data (title, category, price, description, and generated datetime) in an SQLite database.
3. *Implementation:*
   - Define a function fetch_product_data(product_id) that fetches product data for a given product ID from the API. Handle both successful and failed requests.
   - Create an SQLite database named 'products.db'.
   - Define a function create_products_table(cursor) that creates a products table with columns for product information (title, category, price, description) and a date_added column for the generated datetimes.
   - Define a function insert_product_into_db(cursor, product_data) that inserts a product's data along with a generated datetime into the products table.
   - In the __main__ section, use the defined functions to fetch product data, generate random datetimes, and store the information in the database.
   - Print a message indicating the success or failure of data retrieval and insertion.
4. *Challenge:*
   - Modify the script to prompt the user for the range of product IDs they want to fetch and store.
   - Enhance the script to calculate and store the total cost of each product (price multiplied by quantity) in the database.
