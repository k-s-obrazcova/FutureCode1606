import uvicorn
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

@app.get("/animals")
async def all_animals(db: Session = Depends(get_db)):
    animals = db.query(models.Animal).all()
    return {"data": animals}

@app.get("/animals/{id}")
async def one_animal(id: int, db: Session = Depends(get_db)):
    animal = db.query(models.Animal).filter(models.Animal.id == id).first()

    if animal == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"animal with id: {id} does not exist"
        )
    return {"data": animal}

@app.post("/animals", status_code=status.HTTP_201_CREATED)
async def create_animal(animal: schemas.CreateAnimal, db: Session = Depends(get_db)):
    new_animal = models.Animal(**animal.model_dump())
    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)

    return {"message": "animal created", "data": new_animal}

@app.get("/keepers", response_model=list[schemas.Keeper])
async def all_keepers(db: Session = Depends(get_db)):
    keepers = db.query(models.Keeper).all()
    return keepers


@app.post("/keepers", status_code=status.HTTP_201_CREATED)
async def create_keeper(keeper: schemas.Keeper, db: Session = Depends(get_db)):
    new_keeper = models.Keeper(**keeper.model_dump())
    db.add(new_keeper)
    db.commit()
    db.refresh(new_keeper)

    return {"message": "keeper created", "data": new_keeper}

@app.put("/connection/{id_animal}/{id_keeper}")
async def update_full_animal(id_animal: int,id_keeper: int, db: Session = Depends(get_db)):
    animal = db.query(models.Animal).filter(models.Animal.id == id_animal)
    keeper = db.query(models.Keeper).filter(models.Keeper.id == id_keeper)
    animal.first().keeper_id = keeper.first().id
    db.commit()
    return {"data": "Done"}
