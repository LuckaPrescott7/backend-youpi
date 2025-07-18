from fastapi import APIRouter, Depends
from .. import schemas, crud
from ..auth import get_db

router = APIRouter()

@router.post("/newsletter")
def newsletter(data: schemas.NewsletterCreate, db=Depends(get_db)):
    return crud.create_newsletter(db, data)
