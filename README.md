# 📜 Simple Quotes API – Django REST Framework

A lightweight Django REST API that allows users to:

- 🔹 Retrieve a list of inspirational quotes
- 🔹 Add new quotes via POST requests

This project uses **in-memory** or **file-based storage** (no database) and is built with **Django REST Framework**.

---

## 🚀 Live Demo

🔗 [Visit the API on Render](https://quotes-api-50ku.onrender.com))  
https://quotes-api-50ku.onrender.com

---

## 📂 Endpoints

| Method | Endpoint     | Description             |
|--------|--------------|-------------------------|
| GET    | `/quotes/`   | Get a list of quotes    |
| POST   | `/quotes/`   | Add a new quote         |

### ✅ POST request format (JSON):
```json
{
  "quote": "Your quote here",
}
