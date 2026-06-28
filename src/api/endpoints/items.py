from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.deps import get_db, get_current_user
from src.crud.crud_item import get_items, create_user_item
from src.schemas.item import Item, ItemCreate
from src.models.user import User as UserModel

router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=Item)
def create_item(
    item_in: ItemCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    item = create_user_item(db=db, item=item_in, user_id=current_user.id)
    return item
