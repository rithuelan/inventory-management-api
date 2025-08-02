# 🐞 Bug Report

## Summary
Bugs found during manual or automated testing.

| ID  | Description                                        | Steps to Reproduce                          | Expected Result         | Actual Result           | Status   |
|-----|----------------------------------------------------|---------------------------------------------|--------------------------|--------------------------|----------|
| B1  | PUT allows multiple stock updates on same day      | PUT product with different stock twice      | 400 Bad Request          | 200 OK                   | Open     |
| B2  | Invalid category not handled properly              | POST with category = "furniture"            | 400 Bad Request          | 200 OK                   | Fixed    |
| B3  | Error message not descriptive for invalid inputs   | POST with missing fields                    | Descriptive error        | Generic 400 Bad Request  | Fixed    |

# Bug Report: Inventory Management API

## Bug #1: Multiple Stock Updates in One Day Allowed

### ❗ Description:
The API allows stock to be updated more than once per calendar day.

### 🔄 Steps to Reproduce:
1. POST a product.
2. PUT to update stock to 10.
3. PUT again to update stock to 12.

### ✅ Expected Result:
Second stock update should be rejected with 400 error.

### ❌ Actual Result:
Stock updated multiple times.

### 💡 Suggested Fix:
Track last stock update date in product data, compare before allowing update.

---

## Bug #2: Invalid Category Not Rejected

### ❗ Description:
API accepts invalid category like "shoes".

### 🔄 Steps:
POST with `category: "shoes"`

### ✅ Expected:
400 Bad Request.

### ❌ Actual:
Product created.


