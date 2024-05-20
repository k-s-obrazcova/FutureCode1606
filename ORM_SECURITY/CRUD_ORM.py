import uvicorn
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import sessionLocal, engine, get_db
from passlib.context import CryptContext
from . import utils, auth, oauth2

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
app.include_router(auth.router)

@app.get("/users", status_code=status.HTTP_200_OK)
def all_user(db: Session = Depends(get_db)):
    users = db.query(models.Keeper).all()
    return users

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.Keeper, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.Keeper(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users/{id}", response_model=schemas.KeeperOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.Keeper).get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User({id}) not found!"
        )
    return user

@app.get("/animals/verify")
async def all_animal_verify(
        db: Session = Depends(get_db),
        get_current_user: int = Depends(oauth2.get_current_keeper)):
    animals = db.query(models.Animal).all()
    return {"animals": animals}

@app.post("/posts/verify", status_code=status.HTTP_201_CREATED)
async def create_animal(
        animal: schemas.Animal,
        db: Session = Depends(get_db),
        get_current_user: int = Depends(oauth2.get_current_keeper)):
    new_animal = models.Animal(**animal.model_dump())
    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)

    return {"message":"animal created", "data": new_animal}

if __name__ == "__main__":
    uvicorn.run(app)
