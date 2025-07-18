from fastapi import APIRouter, Depends
from .. import schemas, crud
from ..auth import get_db

router = APIRouter()

@router.post("/contact")
def contact(data: schemas.ContactCreate, db=Depends(get_db)):
    return crud.create_contact(db, data)
