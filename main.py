from typing import Optional
import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

books = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel"),
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"sum": a + b}

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books/", response_model=list[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise fastapi.HTTPException(status_code=404, detail="Book not found")