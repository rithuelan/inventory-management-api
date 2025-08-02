from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }

# Create the database
with app.app_context():
    db.create_all()

# Add a product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201

# Get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

# Get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

# Update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 201


# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
