# Book Tracker API

FastAPI + SQLModel + SQLite example for a simple Books CRUD API.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open docs: http://localhost:8000/docs

## Structure

```
main.py       # app startup + seed data
models.py     # SQLModel Book
routes/
    books.py    # /books routes
database.py   # engine, session, create tables
```

## Endpoints

- GET /           — welcome
- POST /books     — create book
- GET /books      — list books
- GET /books/{id} — get book
- DELETE /books/{id} — delete book

## Database

- SQLite file at `./books.db`
- URL format: `sqlite:///./books.db` (SQLAlchemy-style)

—

Enjoy! 🚀
