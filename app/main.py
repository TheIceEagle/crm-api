# app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db import session as db_session
# from app.db import init_db # We might not need init_db.py for table creation anymore
# from app.models.user import User # No longer needed here for Base.metadata.create_all

# API Routers will be added later
# from app.api.api_v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# REMOVE OR COMMENT OUT THE STARTUP EVENT FOR DB INITIALIZATION
# @app.on_event("startup")
# def on_startup():
#     temp_db = db_session.SessionLocal()
#     try:
#         # init_db.init_db(temp_db) # This function will no longer create tables
#         # Instead, you might use init_db for creating initial data if needed,
#         # after migrations have run.
#         print("Application startup. Ensure database migrations are applied.")
#     finally:
#         temp_db.close()

@app.get("/")
async def read_root():
    return {"message": f"Hello World, welcome to {settings.PROJECT_NAME}!"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

# Example placeholder (will be replaced by actual user endpoints)
@app.get("/users/me", summary="Get current user (example - not functional yet)")
async def read_users_me(db: Session = Depends(db_session.get_db)):
    return {"message": "This endpoint will show current user details. DB session is available."}

# Include API routers (we will create these later)
# app.include_router(api_router, prefix=settings.API_V1_STR)

