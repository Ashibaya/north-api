from typing import List, Optional

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    login: str
    role_id: int
    phone: Optional[str] = None
    fio: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
    login: Optional[str] = None
    fio: Optional[str] = None


class TokenData(BaseModel):
    login: Optional[str] = None
