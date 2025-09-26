from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 65000},
    {"id": 2, "name": "Smartphone", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

@app.route('/')
def home():
    return "Welcome to Product Service!"

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
