from flask import Flask, jsonify, request
from database import init_db
init_db()

app = Flask(__name__)

# In-memory store for flavors (for demonstration)
flavors = ["Vanilla", "Chocolate", "Strawberry"]

@app.route('/flavors', methods=['GET'])
def get_flavors():
    """Retrieve all flavors."""
    return jsonify({'flavors': flavors})

@app.route('/flavors', methods=['POST'])
def add_flavor():
    """Add a new flavor."""
    data = request.get_json()
    new_flavor = data.get('flavor')
    if new_flavor:
        flavors.append(new_flavor)
        return jsonify({'message': 'Flavor added', 'flavors': flavors}), 201
    else:
        return jsonify({'error': 'No flavor provided'}), 400

if __name__ == '__main__':
    # Running on port 5000; accessible to Docker
    app.run(host='0.0.0.0', port=5000)
