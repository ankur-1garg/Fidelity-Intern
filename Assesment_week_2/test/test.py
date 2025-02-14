import requests


def get_products_dict():
    API_URL = "http://127.0.0.1:8000/api/products/"

    try:
        # Send GET request to the API
        response = requests.get(API_URL)

        # Check if request was successful
        if response.status_code == 200:
            # Convert JSON response to dictionary with ID as key
            products = response.json()
            products_dict = {product["id"]: product for product in products}

            # Print the dictionary
            print("\nProducts Data (Dictionary Format):")
            for pid, product in products_dict.items():
                print(f"\nProduct ID: {pid}")
                print(f"Name: {product['name']}")
                print(f"Description: {product['description']}")
                print(f"Price: ${product['price']}")
                # Changed from 'stock' to 'quantity'
                print(f"Quantity: {product['quantity']}")
                print(f"Created At: {product['created_at']}")

            return products_dict

        else:
            print(
                f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


if __name__ == "__main__":
    # Get products in dictionary format
    products_dict = get_products_dict()

    if products_dict:
        # Example: Accessing a specific product by ID
        first_id = list(products_dict.keys())[0]
        print(f"\nAccessing product with ID {first_id}:")
        print(f"Name: {products_dict[first_id]['name']}")
