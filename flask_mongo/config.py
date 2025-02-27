from pymongo import MongoClient
from urllib.parse import quote_plus

# Escape username and password
username = quote_plus("ankurgarg2392004")
password = quote_plus("Ankur@23")

# Construct the MongoDB URI with escaped credentials
uri = f"mongodb+srv://{username}:{password}@demo.veiek.mongodb.net/?retryWrites=true&w=majority&appName=demo"

# Connect to MongoDB
client = MongoClient(uri)
db = client['demo']
collection = db['users']

# Test the connection
try:
    client.server_info()
    print("Successfully connected to MongoDB!")
except Exception as e:
    print("Failed to connect to MongoDB")
    print(f"Error: {e}")