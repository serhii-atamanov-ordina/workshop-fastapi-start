from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_database

# Replace these values with your actual secret key and algorithm
SECRET_KEY = "workshop"
ALGORITHM = "HS256"

# OAuth2PasswordBearer with async support
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to decode JWT token
async def decode_token(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_database)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        pass
    except JWTError:
        raise credentials_exception


if __name__ == "__main__":
    # Payload (data you want to include in the token)
    payload = {"name": "user", "password": "fastapi"}

    # Generate the token
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    print("Generated Token:", token)
