from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import database, schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(keeper_credential: schemas.KeeperLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.Keeper).filter(models.Keeper.email == keeper_credential.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Неудачное получение данных"
        )
    if not utils.verify(keeper_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Не верный пароль"
        )
    access_token = oauth2.create_access_token(data={"keeper_id": user.id})
    return  {"access_token": access_token, "token_type": "bearer"}

@router.post("/login/oauth")
def login_oauth(keeper_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Keeper).filter(models.Keeper.email == keeper_credential.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Неудачное получение данных"
        )
    if not utils.verify(keeper_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Не верный пароль"
        )
    access_token = oauth2.create_access_token(data={"keeper_id": user.id})
    return  {"access_token": access_token, "token_type": "bearer"}