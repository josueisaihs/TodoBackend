from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext

from db.client import db_client
from db.models.user import User as UserModel
from db.models.token import TokenData
from config.settings import Settings
from db.schemas.user import user_schema

settings = Settings()

SECRET_KEY = settings.secret_key
ACCESS_TOKEN_DURATION = settings.access_token_duration
ALGORITHM = settings.algorithm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_context = OAuth2PasswordBearer(tokenUrl="api/login")


def verify_password(plain_password: str, password: str) -> bool:
    return pwd_context.verify(plain_password, password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(username: str) -> UserModel:
    user = user_schema(db_client.users.find_one({"email": username}))
    return UserModel(**user)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta|None=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_token(username, password):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_DURATION)
    return create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )