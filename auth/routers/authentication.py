from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import token
from auth.login.models import login as models
from auth.login.repository import login as resp
from auth import database
from auth.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user_list = [resp.get_user_by_email(db, request.username),
                 resp.get_user_by_login(db, request.username),
                 resp.get_user_by_phone(db, request.username)]
    user = next((user for user in user_list if user is not None), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer", "login": user.login, "fio": user.fio, "id": user.id}
