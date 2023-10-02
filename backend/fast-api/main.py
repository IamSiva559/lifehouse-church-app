from fastapi import FastAPI
import uvicorn
from api.helpers.database import close_database_connection
from api.login import router as login_router
from api.logout import router as logout_router
from api.create_user import router as create_router
from api.update_user import router as update_router


# Create a FastAPI instance
app = FastAPI()

# Include the router modules with appropriate prefixes and tags
app.include_router(login_router, prefix="/auth", tags=["login"])
app.include_router(logout_router, prefix="/auth", tags=["logout"])
app.include_router(create_router, prefix="/users", tags=["create"])
app.include_router(update_router, prefix="/users", tags=["update"])


# Close the database connection when the application shuts down
@app.on_event("shutdown")
async def shutdown_db_client():
    close_database_connection()

if __name__ == "__main__":
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#To run app
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
