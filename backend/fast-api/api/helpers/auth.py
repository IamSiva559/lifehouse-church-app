from datetime import datetime, timedelta
from typing import Optional
import jwt
from fastapi import HTTPException
import config
from jose import JWTError, jwt
from fastapi import HTTPException, Depends,security
from fastapi.security import OAuth2PasswordBearer,HTTPAuthorizationCredentials,HTTPBearer
import config

security = HTTPBearer()

def create_access_token(data: str, expires_delta: timedelta):
    # Create a payload with the custom claims (mobile and email)
    payload = {
        "exp": datetime.utcnow() + expires_delta,
        "email_mobile": data
    }
    print(payload)
    encoded_jwt = jwt.encode(payload, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

def verify_token(token: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, config.SECRET_KEY, algorithms=[config.ALGORITHM])

        # Check if the token has expired
        current_time = datetime.utcnow()
        if "exp" in payload:
            expiration_time = datetime.utcfromtimestamp(payload["exp"])
            if expiration_time < current_time:
                raise HTTPException(status_code=401, detail="Token has expired")

        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid or has expired")


    # additional custom checks can go here

    return decoded_token



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        current_time = datetime.utcnow()
        
        # Check if the token has expired
        if "exp" in payload and datetime.utcfromtimestamp(payload["exp"]) < current_time:
            raise HTTPException(status_code=401, detail="Token has expired")

        # Extract the user's mobile and email from the token payload
        email_mobile = payload.get("email_mobile")
        if email_mobile:
            return email_mobile
        else:
            raise HTTPException(status_code=400, detail="Token does not contain mobile or email")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token: Expired or Invalid")



