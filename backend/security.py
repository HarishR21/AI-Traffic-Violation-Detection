from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os
from sqlalchemy.orm import Session
from database import get_db
from models import Admin  # Assuming you have an Admin model

# Secret key for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

# Request model
class LoginRequest(BaseModel):
    username: str
    password: str

# Token Response Model
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.username == request.username).first()
    
    if not admin or not pwd_context.verify(request.password, admin.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    token_data = {"sub": request.username, "exp": datetime.utcnow() + timedelta(hours=2)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}
