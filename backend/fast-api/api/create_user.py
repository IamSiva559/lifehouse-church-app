from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from passlib.context import CryptContext
from datetime import datetime
import config 
from api.helpers import database

router = APIRouter()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    name: str
    email: str
    mobile: str
    date_of_birth: str
    location: str
    password: str
    confirm_password: str
    address: str

@router.post("/create", response_model=dict)
async def create_user(user_data: UserCreate):
    # Check if the email or mobile is already registered
    existing_user = database.users_collection.find_one(
        {"$or": [{"email": user_data.email}, {"mobile": user_data.mobile}]}
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Email or mobile already registered")

    # Check if the password and confirm_password match
    if user_data.password != user_data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Hash the password before storing it
    hashed_password = pwd_context.hash(user_data.password)

    # Create the new user document
    new_user = {
        "name": user_data.name,
        "email": user_data.email,
        "mobile": user_data.mobile,
        "date_of_birth": user_data.date_of_birth,
        "location": user_data.location,
        "password": hashed_password,
        "address": user_data.address 
    }

    # Insert the new user into the MongoDB collection
    result = database.users_collection.insert_one(new_user)

    if result.acknowledged:
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=500, detail="User creation failed")
