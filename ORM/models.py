from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    age = Column(Integer, nullable=True)

    keeper_id = Column(Integer, ForeignKey("keepers.id"))
    keeper = relationship("Keeper", back_populates="animals")

class Keeper(Base):
    __tablename__ = "keepers"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    animals = relationship("Animal", back_populates="keeper")
