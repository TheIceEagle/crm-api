# app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db import session as db_session # Renamed for clarity
from app.db import init_db # Import the init_db function
from app.models.user import User # Ensure User model is imported for table creation
# We will add API routers later
# from app.api.endpoints import users, login

# Create a FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME if hasattr(settings, 'PROJECT_NAME') else "My Awesome FastAPI App",
    version=settings.PROJECT_VERSION if hasattr(settings, 'PROJECT_VERSION') else "0.2.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json" if hasattr(settings, 'API_V1_STR') else "/openapi.json"
)

# This is a simple way to create DB tables at startup for development.
# For production, you should use Alembic migrations.
@app.on_event("startup")
def on_startup():
    # Create a temporary session to initialize the DB
    # This is just for the initial table creation
    temp_db = db_session.SessionLocal()
    try:
        init_db.init_db(temp_db) # Call the init_db function
        print("Database tables initialized (if they didn't exist).")
    finally:
        temp_db.close()


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": f"Hello World, welcome to {settings.PROJECT_NAME if hasattr(settings, 'PROJECT_NAME') else 'my app'}!"}

@app.get("/ping")
async def ping():
    """
    A simple health check endpoint.
    """
    return {"message": "pong"}

# Example: How to use the database session in an endpoint
@app.get("/users/me", summary="Get current user (example - not functional yet)")
async def read_users_me(db: Session = Depends(db_session.get_db)):
    # This is just a placeholder to show db dependency.
    # Actual user retrieval will be implemented later.
    return {"message": "This endpoint will show current user details. DB session is available."}

# We will include routers later:
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(login.router, prefix="/api/v1/login", tags=["login"])

