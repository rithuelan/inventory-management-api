# Inventory Management API

This is a RESTful Inventory Management API built with Flask (Python). It supports full CRUD operations with custom business rules and validation.

## 🛠 Features

- Create, read, update, and delete products.
- Business rules:
  - Valid categories: `electronics`, `books`, `clothing`.
  - Electronics must have a price ≥ 10.
  - Stock updates allowed once per calendar day.
- JSON request and response format.
- In-memory storage.

---

## 🚀 How to Run the API
IN VSCODE:

.\venv\Scripts\activate
python app.py
in postman:

 -curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d "{\"product_id\":\"1\", \"category\":\"electorins\", \"name\":laptop\"stock\":20}"

