from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError
import requests

app = Flask(__name__)

# Define a Pydantic model for input validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.route('/')
def hello():
    return "Hello, World! Welcome to the Python Flask App!"

@app.route('/items', methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        item = Item(**data)
        return jsonify(item.dict()), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

@app.route('/external', methods=['GET'])
def external_api():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to fetch external API"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
