import requests


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
