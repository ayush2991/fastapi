from fastapi import FastAPI
from routes.books import router as books_router
from database import create_db_and_tables, get_session
from models import Book
from sqlmodel import Session, select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    # Create tables if they don't exist
    create_db_and_tables()

    # Insert initial data if table is empty
    with next(get_session()) as session:
        existing_books = session.exec(select(Book)).all()
        if not existing_books:
            book1 = Book(title="1984", author="George Orwell", description="Dystopian novel")
            book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel on justice")
            session.add_all([book1, book2])
            session.commit()
            print("✅ Initialized database with 2 sample books.")

app.include_router(books_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Book Tracker API with SQLite!"}
