from flask import Flask, jsonify, request
from database import init_db
init_db()

app = Flask(__name__)

# In-memory inventory data (flavor: quantity)
inventory = {
    "Vanilla": 20,
    "Chocolate": 15,
    "Strawberry": 10
}

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify({"inventory": inventory})

@app.route('/inventory/<flavor>', methods=['PUT'])
def update_inventory(flavor):
    data = request.get_json()
    quantity = data.get("quantity")
    if quantity is None:
        return jsonify({"error": "Quantity not provided"}), 400
    inventory[flavor] = quantity
    return jsonify({"message": "Inventory updated", "inventory": inventory})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
