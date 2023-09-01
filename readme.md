**Exercise (request / get data):**Create a Python script that fetches product data from the "Fake Store API" using the `requests` library. The goal is to retrieve and display information about a specific product based on its ID.1. * **Setup:** *

- Install the `requests` library if you haven't already: `pip install requests`2. * **Instructions:** *
- Write a function `fetch_product_data(product_id)` that takes a product ID as an argument and returns the product data as a dictionary.
- Inside the function, use the `requests.get()` function to make a GET request to the API endpoint `<a target="_blank" class="c-link" data-stringify-link="https://fakestoreapi.com/products/{product_id}" delay="150" data-sk="tooltip_parent" href="https://fakestoreapi.com/products/%7Bproduct_id%7D" rel="noopener noreferrer">https://fakestoreapi.com/products/{product_id}</a>`.
- Check if the response status code is 200 (OK). If it is, use `response.json()` to parse the JSON response and return the product data dictionary. If not, print an error message.3. * **Output:** *
- If the function successfully fetches the product data, print the following information:
  - Product Name
  - Product Category
  - Product Price
  - Product Description
- If the function fails to fetch the product data, print an error message.
