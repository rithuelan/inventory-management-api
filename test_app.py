import requests

BASE_URL = "http://127.0.0.1:5000/products"

# ✅ CREATE a product
response = requests.post(BASE_URL, json={
    "name": "iPhone",
    "category": "electronics",
    "price": 1000,
    "stock": 50
})
print("Create:", response.status_code, response.json())

# ✅ GET all products
response = requests.get(BASE_URL)
print("All Products:", response.status_code, response.json())

# ✅ UPDATE a product
response = requests.put(BASE_URL + "/1", json={
    "stock": 55
})
print("Update:", response.status_code, response.json())

# ✅ DELETE a product
response = requests.delete(BASE_URL + "/1")
print("Delete:", response.status_code, response.text)
