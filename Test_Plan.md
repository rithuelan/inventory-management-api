# 📋 Test Plan

## Objective
To verify that all API endpoints in the Inventory Management system function correctly, enforce business rules, and handle edge cases properly.

## Test Scope
- API Endpoints (`GET`, `POST`, `PUT`, `DELETE`)
- Business Rules
- Input Validations
- Response Codes

## Test Environment
- OS: Windows 10+
- Python Version: 3.13
- Testing Tool: pytest
- Flask Version: (mention your Flask version)

## Test Cases

| ID  | Endpoint        | Method | Description                      | Expected Result        |
|-----|------------------|--------|----------------------------------|------------------------|
| TC1 | /products        | GET    | Retrieve all products            | 200 OK + JSON List     |
| TC2 | /products        | POST   | Create valid product             | 201 Created            |
| TC3 | /products/{id}   | GET    | Retrieve product by ID           | 200 OK / 404 Not Found |
| TC4 | /products/{id}   | PUT    | Update product details           | 200 OK / 404 Not Found |
| TC5 | /products/{id}   | DELETE | Delete product                   | 200 OK / 404 Not Found |
| TC6 | /products        | POST   | Invalid category                 | 400 Bad Request        |
| TC7 | /products        | POST   | Electronics with price < 10      | 400 Bad Request        |
| TC8 | /products/{id}   | PUT    | Stock updated more than once/day| 400 Bad Request        |


## 1. Objectives
- Ensure all CRUD operations work correctly.
- Validate all business rules (name, category, price, stock rules).
- Check edge cases and negative inputs.
- Confirm correct HTTP status codes and JSON responses.

## 2. Scope
- Backend API (no frontend).
- Manual and automated tests (using Postman/pytest).

## 3. Test Scenarios

### ✅ Create Product (POST /products)
- Valid product with all required fields.
- Missing `name`, `category`, or `price`.
- Invalid `category` (not in allowed list).
- `price` < 10 when `category = electronics`.

### ✅ Read Product (GET /products and /products/{id})
- Get all products.
- Get product by valid ID.
- Get product by invalid ID (expect 404).

### ✅ Update Product (PUT /products/{id})
- Update `price` and `stock` of existing product.
- Try updating `stock` twice on same day (should fail).
- Update product with invalid data (e.g., negative stock).

### ✅ Delete Product (DELETE /products/{id})
- Delete existing product.
- Delete already deleted/non-existent product (expect 404).

## 4. Test Data
- Valid product:  
  `{ "name": "Laptop", "category": "electronics", "price": 1000, "stock": 10 }`
- Invalid product:  
  `{ "name": "", "category": "shoes", "price": -1, "stock": -5 }`
- Edge case:  
  Long name (100+ characters), zero stock, zero price (non-electronics)

## 5. Tools
- Postman (for manual testing)
- Pytest + requests (for automation)

## 6. Notes
- Use UTC date for stock update rules.
- Data is in-memory (no DB persistence).
