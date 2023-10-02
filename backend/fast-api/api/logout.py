# logout.py

from fastapi import APIRouter, HTTPException, Depends
import config 
from jose import jwt
from jose.exceptions import JWTError

router = APIRouter()


# Secret key for decoding JWT tokens
SECRET_KEY = config.SECRET_KEY

# Token algorithm
ALGORITHM = config.ALGORITHM

# Function to get the current user based on the JWT token
def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# Invalidation set for revoked tokens
revoked_tokens = set()

@router.post("/logout")
async def logout(
    current_user: dict = Depends(get_current_user)
):
    try:
        # Get the token from the current_user
        token = current_user.get("token")

        # Check if the token is already in the revoked tokens set
        if token in revoked_tokens:
            raise HTTPException(status_code=400, detail="Token already revoked")

        # Add the token to the revoked tokens set
        revoked_tokens.add(token)

        # You can also implement further invalidation logic if needed, such as blacklisting the user's refresh token.

        return {"message": "Logout successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred during logout")



