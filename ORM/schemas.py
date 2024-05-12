from pydantic import BaseModel
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