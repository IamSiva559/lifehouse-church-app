from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
import config 
from jose import JWTError, jwt
from api.helpers.auth import verify_token,get_current_user
from api.helpers.database import users_collection

router = APIRouter()

class UserUpdate(BaseModel):
    name: str
    email: str
    mobile: str
    date_of_birth: str
    location: str
    address: str

# Update user details route
@router.put("/update", response_model=dict, dependencies=[Depends(verify_token)])
async def update_user(
    user_data: UserUpdate,
    current_user: str = Depends(get_current_user)
):
    print(current_user)
    existing_user = users_collection.find_one({"$or": [{"mobile": current_user}, {"email": current_user}]})
    
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the user document
    updated_user = {
        "name": user_data.name,
        "email": user_data.email,
        "mobile": user_data.mobile,
        "date_of_birth": user_data.date_of_birth,
        "location": user_data.location,
        "address": user_data.address
    }

    # Update the user in the MongoDB collection
    result = users_collection.update_one({"$or": [{"mobile": current_user}, {"email": current_user}]}, {"$set": updated_user})

    if result.modified_count > 0:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="User update failed")
