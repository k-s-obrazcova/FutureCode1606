from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP,text
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
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('current_timestamp'))

    animals = relationship("Animal", back_populates="keeper")
