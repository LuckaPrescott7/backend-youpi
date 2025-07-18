from fastapi import APIRouter, Depends
from .. import schemas, crud
from ..auth import get_db

router = APIRouter()

@router.post("/comment")
def add_comment(data: schemas.CommentCreate, db=Depends(get_db)):
    return crud.create_comment(db, data)
