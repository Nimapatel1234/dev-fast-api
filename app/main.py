from fastapi import FastAPI
from .routers import (
    auth_user,
    books,
    authors,
    groups,
    permissions,
    bookshelves,
    subjects,
)

# Initialize FastAPI app
app = FastAPI(
    title="Existing Database API",
    description="API connected to an existing PostgreSQL database.",
    version="1.0.0",
)

# Include routers
app.include_router(auth_user.router, prefix="/users", tags=["Users"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(permissions.router, prefix="/permissions", tags=["Permissions"])
app.include_router(bookshelves.router, prefix="/bookshelves", tags=["Bookshelves"])
app.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])
