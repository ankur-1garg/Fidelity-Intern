from flask import Flask, request, jsonify
from config import client, db, collection
from bson import ObjectId

app = Flask(__name__)

# Create - POST
@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        result = collection.insert_one(user_data)
        return jsonify({"message": "User created", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Read - GET all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = list(collection.find())
        # Convert ObjectId to string for JSON serialization
        for user in users:
            user['_id'] = str(user['_id'])
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Read - GET single user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = collection.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Update - PUT
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.get_json()
        result = collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': user_data}
        )
        if result.modified_count:
            return jsonify({"message": "User updated"}), 200
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete - DELETE
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        result = collection.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count:
            return jsonify({"message": "User deleted"}), 200
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)