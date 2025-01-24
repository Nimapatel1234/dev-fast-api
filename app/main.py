from fastapi import FastAPI
from sqlalchemy import create_engine
from .database import Base, engine
from .routers import books, authors, users, groups, permissions

# Initialize the database
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI(
    title="Books API",
    description="API for managing books, authors, users, groups, and permissions.",
    version="1.0.0",
)

# Test database connection during startup
@app.on_event("startup")
async def startup_event():
    try:
        with engine.connect() as connection:
            print("Database connection successful!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

# Include routers
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(permissions.router, prefix="/permissions", tags=["Permissions"])
