# dependencies.py

from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal, get_db
from services import create_item, get_item, get_items
from schemas import ItemCreate, ItemResponse
from models import Item

def get_item_service(db: Session = Depends(get_db)):
    return get_item(db)

def get_items_service(db: Session = Depends(get_db)):
    return get_items(db)

def create_item_service(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(item=item, db=db)
