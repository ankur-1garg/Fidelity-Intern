from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Data store
res = {
    1: {"first": 1},
    2: {"second": 2},
    3: {"third": 3}
}

# Resource class for handling items
class Item(Resource):
    def get(self, item_id):
        if item_id in res:
            return res[item_id], 200
        return {"message": "Item not found"}, 404

    def put(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=dict, required=True)
        args = parser.parse_args()
        
        res[item_id] = args['value']
        return res[item_id], 201

    def delete(self, item_id):
        if item_id in res:
            del res[item_id]
            return '', 204
        return {"message": "Item not found"}, 404

# Resource class for handling the collection
class ItemList(Resource):
    def get(self):
        return res, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=dict, required=True)
        args = parser.parse_args()
        
        item_id = max(res.keys()) + 1
        res[item_id] = args['value']
        return res[item_id], 201

# Register routes
api.add_resource(Item, '/api/items/<int:item_id>')
api.add_resource(ItemList, '/api/items')

@app.route('/')
def home():
    return render_template('home.html', data=res)

# Add a new route to get all keys
@app.route('/api/keys')
def get_keys():
    return {"keys": list(res.keys())}, 200

if __name__ == '__main__':
    app.run(debug=True)