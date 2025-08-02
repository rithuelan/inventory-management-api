import requests

BASE_URL = "http://127.0.0.1:5000/products"

# Step 1: Get all existing products
response = requests.get(BASE_URL)
products = response.json()

# Step 2: Delete each product
for product in products:
    product_id = product['id']
    del_response = requests.delete(f"{BASE_URL}/{product_id}")
    print(f"Deleted product {product_id}: {del_response.status_code}")

# Step 3: Add fresh 5 products
new_products = [
    {"name": "Laptop", "category": "electronics", "price": 1200.50, "stock": 10},
    {"name": "Shirt", "category": "clothing", "price": 25.99, "stock": 50},
    {"name": "Book", "category": "books", "price": 15.00, "stock": 100},
    {"name": "Smartphone", "category": "electronics", "price": 800.00, "stock": 20},
    {"name": "Jeans", "category": "clothing", "price": 40.00, "stock": 30},
]

for prod in new_products:
    add_response = requests.post(BASE_URL, json=prod)
    print(f"Added: {add_response.json()}")
