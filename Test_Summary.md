# Test Summary & Reflection

## ✅ Test Coverage Summary
- Covered all CRUD endpoints (GET, POST, PUT, DELETE).
- Validated all business rules:
  - Name presence and length
  - Category allowed values
  - Price constraints (especially for electronics)
  - Stock update once per day
- Tested edge cases (empty, long values, zero price/stock)

## ❗ Bugs Found
- Multiple stock updates in one day were incorrectly allowed.
- Category validation missing.
- Some 404 and 400 errors not consistently returned.

## 💭 Challenges Faced
- Implementing the stock-update-per-day constraint.
- Tracking validation messages in consistent format.

## 🔍 Lessons Learned
- Importance of strict input validation.
- Realizing how edge cases break assumptions.
- API testing benefits greatly from automation.

## ✅ What Could Be Improved
- Use a real database (like SQLite or PostgreSQL) for persistence.
- Add API rate-limiting and authentication.
- Include timestamps/logging for better debugging.

## 📌 Future Suggestions
- Add pagination for GET /products.
- Add filtering by category or price range.
- Frontend dashboard to visualize inventory.
