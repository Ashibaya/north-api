from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas import login as schemas
from ..models import login as models
from auth.hashing import Hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()


def delete_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    now_hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(
        email=user.email,
        login=user.login,
        phone=user.phone,
        fio=user.fio,
        hashed_password=now_hashed_password,
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserCreate):
    vals = user.dict()
    model = models.User(**user.dict())
    db_user = db.query(models.User).filter(id == model.id)
    if not db_user.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    db_user.update(vals)
    db.commit()
    return model

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()


def get_role(db: Session, id: int):
    return db.query(models.Role).filter(models.Role.id == id).first()


def delete_role(db: Session, id: int):
    role = db.query(models.Role).filter(models.Role.id == id)
    if not role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")
    role.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_role(db: Session, role: schemas.RoleCreate):
    vals = role.dict()
    model = models.Role(**role.dict())
    db_role = db.query(models.Role).filter(id == model.id)
    if not db_role.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")
    db_role.update(vals)
    db.commit()
    return model

def create_roles(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
