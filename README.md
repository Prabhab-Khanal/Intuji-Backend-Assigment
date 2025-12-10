# Intuji Backend Assignment

This repository contains two parts:

1. A **Blog API** built using **Python, FastAPI, SQLAlchemy, and SQLite**
2. An algorithm that finds **all number pairs in a list that sum to a target value**

All Python files follow **PEP 8** and **PEP 257** coding standards.

---

## Clone the Repository

```bash
git clone https://github.com/Prabhab-Khanal/Intuji-Backend-Assigment
```

## Part 1: Blog API (FastAPI)

### Features
- **GET /blogs** — Get all blogs  
- **GET /blogs/{id}** — Get a specific blog  
- **POST /blogs** — Create a new blog  
- **PUT /blogs/{id}** — Update a blog  

Database used: **SQLite**  
API located in the `app/` folder.

---

## How to Run the API

1. Create and Activate virtual environment:

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
uvicorn app.main:app --reload
```

4. Open the API docs:

```
http://127.0.0.1:8000/docs
```

You can test all endpoints from Swagger UI or import the included Postman collection.

---

## Part 2: Pair Sum Algorithm

A simple script that checks a list of numbers and prints all pairs whose sum equals a given target.

### How to Run

```bash
python algorithm/sum_pair.py
```

### Example Output

```
Pairs found: [(8, 2), (7, 3)]
```

---

## Notes

* Project uses PEP 8 naming, formatting, and clean structure.
* SQLite database file is generated automatically.
* Postman collection is included in the `postman/` folder.

---


