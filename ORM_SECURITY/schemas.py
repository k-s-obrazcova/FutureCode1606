from pydantic import BaseModel, EmailStr
from typing import Optional


class AnimalBase(BaseModel):
    name: str
    species: str
    age: Optional[int] = None


class UpdateAnimal(AnimalBase):
    age: Optional[int]


class CreateAnimal(AnimalBase):
    pass


class Animal(BaseModel):
    name: str
    species: str
    age: Optional[int]

    class Config:
        orm_mode = True


class Keeper(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class KeeperLogin(BaseModel):
    email: EmailStr
    password: str

class KeeperOut(BaseModel):
    id: int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

