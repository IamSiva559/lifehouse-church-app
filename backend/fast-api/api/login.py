from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import config
from api.helpers import database
from api.helpers.auth import create_access_token

router = APIRouter()


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserSignIn(BaseModel):
    email_mobile: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=Token)
async def login(user_data: UserSignIn):
    email_mobile = user_data.email_mobile
    password = user_data.password

    # Check if the user exists with the provided email or mobile
    user = database.users_collection.find_one(
        {"$or": [{"email": email_mobile}, {"mobile": email_mobile}]}
    )

    if user and verify_password(password, pwd_context.hash(user["password"])):
        # Generate an access token with a 30-minute expiration
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(email_mobile, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Replace this with your actual password hashing method (e.g., bcrypt)
def verify_password(plain_password, hashed_password):
    # Implement secure password verification here
    return pwd_context.verify(plain_password, hashed_password)

