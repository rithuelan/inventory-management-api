# 📦 Inventory Management API

This is a RESTful Inventory Management API built with **Flask (Python)**. It supports full CRUD operations with custom business rules and validations.

---

## 🛠 Features

- Create, read, update, and delete products
- Enforces the following business rules:
  - Valid categories: `electronics`, `books`, `clothing`
  - If category is `electronics`, price must be **≥ 10**
  - `stock` can be updated only **once per calendar day**
- JSON request and response format
- Uses **SQLite** for storage

## 🚀 How to Run the API

### ✅ Step 1: Set up and activate virtual environment (in VSCode Terminal)

```bash
.\venv\Scripts\activate

✅ Step 2: Run the API

bash ---- python app.py

🧪 Example API Calls (via Postman or curl)
✅ Create Product
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/products \
-H "Content-Type: application/json" \
-d "{\"name\":\"Laptop\", \"category\":\"electronics\", \"price\":1200, \"stock\":20}
