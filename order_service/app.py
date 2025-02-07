from flask import Flask, jsonify, request
from database import init_db
init_db()

app = Flask(__name__)

# In-memory order list for demonstration
orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders})

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = data.get("order")
    if not order:
        return jsonify({"error": "Order details missing"}), 400
    orders.append(order)
    return jsonify({"message": "Order created", "order": order}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
