# Learning FastAPI Step by Step

A hands-on learning project to master FastAPI by building a Books API from scratch.

## What You'll Learn

- Setting up a FastAPI application
- Creating basic routes and endpoints
- Working with path parameters and query parameters
- Using Pydantic models for data validation
- Building a RESTful API with CRUD operations
- Automatic API documentation with Swagger UI
- HTTP status codes and error handling

## Getting Started

### Prerequisites

- Python 3.7+
- Basic understanding of Python and REST APIs

### Setup

1. Create a project directory:
```bash
mkdir fastapi-learning
cd fastapi-learning
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn pydantic
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload on code changes - perfect for development!

## Learning Path

### Step 1: Your First Endpoint

The simplest FastAPI app starts with a single GET endpoint:

```python
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

**Try it:** Visit `http://localhost:8000/`

### Step 2: Query Parameters

Learn how to accept input through query parameters:

```python
@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"sum": a + b}
```

**Try it:** `http://localhost:8000/sum?a=5&b=10`

Notice how FastAPI automatically validates that `a` and `b` are integers!

### Step 3: Data Models with Pydantic

Define structured data using Pydantic models:

```python
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
```

This provides automatic:
- Type validation
- JSON serialization
- API documentation

### Step 4: GET Requests with Path Parameters

Retrieve specific resources using path parameters:

```python
@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Find and return book by ID
```

**Try it:** `http://localhost:8000/books/1`

### Step 5: POST Requests

Create new resources by accepting JSON in the request body:

```python
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book
```

**Try it:**
```bash
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}'
```

### Step 6: Error Handling

Handle cases where resources aren't found:

```python
raise fastapi.HTTPException(status_code=404, detail="Book not found")
```

**Try it:** `http://localhost:8000/books/999`

### Step 7: Interactive API Documentation

FastAPI automatically generates interactive API docs!

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

You can test all endpoints directly from the browser!

## Current API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Hello world endpoint |
| GET | `/sum?a={int}&b={int}` | Add two numbers |
| GET | `/books/` | List all books |
| GET | `/books/{book_id}` | Get a specific book |
| POST | `/books/` | Create a new book |

## Practice Exercises

Try extending the API with these exercises:

1. **Add a DELETE endpoint** - Remove a book by ID
2. **Add a PUT endpoint** - Update an existing book
3. **Add filtering** - Get books by author using query parameters
4. **Add pagination** - Limit and offset for the books list
5. **Add validation** - Ensure book titles are at least 3 characters long

## Key Concepts Learned

✅ **FastAPI basics** - Creating an app and defining routes  
✅ **Type hints** - Python type annotations for validation  
✅ **Pydantic models** - Structured data with automatic validation  
✅ **Path parameters** - Dynamic URL segments  
✅ **Query parameters** - URL query strings  
✅ **Request body** - Accepting JSON data in POST requests  
✅ **Response models** - Defining expected response structure  
✅ **HTTP exceptions** - Proper error handling  
✅ **Auto documentation** - Swagger UI and ReDoc  

## Next Steps

- Add a database (SQLAlchemy)
- Implement authentication (OAuth2, JWT)
- Add background tasks
- Deploy to production
- Write tests with pytest

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

Happy learning! 🚀
