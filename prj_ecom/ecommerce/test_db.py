from pymongo import MongoClient
from urllib.parse import quote_plus
from bson import ObjectId


def test_deletion():
    # MongoDB connection settings
    username = quote_plus('ankurgarg2392004')
    password = quote_plus('Ankur@23')
    host = 'demo.veiek.mongodb.net'

    uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"

    try:
        # Connect to MongoDB
        client = MongoClient(uri)
        db = client.ecom
        collection = db.store_product

        # List all products before deletion
        print("Products before deletion:")
        for product in collection.find():
            print(f"ID: {product['_id']}, Name: {product.get('name')}")

        # Delete a product (replace with actual MongoDB ID)
        mongo_id = "67c07f2bfcd3fe721afea500"  # Example ID
        result = collection.delete_one({'_id': ObjectId(mongo_id)})

        if result.deleted_count:
            print(f"\nProduct with ID {mongo_id} deleted successfully")
        else:
            print(f"\nNo product found with ID {mongo_id}")

        # List all products after deletion
        print("\nProducts after deletion:")
        for product in collection.find():
            print(f"ID: {product['_id']}, Name: {product.get('name')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    test_deletion()
