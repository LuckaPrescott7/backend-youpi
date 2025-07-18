from fastapi import APIRouter, Depends
from .. import schemas, crud
from ..auth import get_db, get_current_user

router = APIRouter()

@router.post("/blog", dependencies=[Depends(get_current_user)])
def create_blog(data: schemas.BlogCreate, db=Depends(get_db)):
    return crud.create_blog(db, data)
