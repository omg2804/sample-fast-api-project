from sqlalchemy.orm import Session
from models import Item
from schemas import ItemCreate, ItemResponse
from database import SessionLocal

def create_item(db: Session, item: ItemCreate) -> ItemResponse:
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return ItemResponse.from_orm(db_item)

def get_item(db: Session, item_id: int) -> ItemResponse:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    return ItemResponse.from_orm(db_item) if db_item else None

def get_items(db: Session, skip: int = 0, limit: int = 10) -> list[ItemResponse]:
    items = db.query(Item).offset(skip).limit(limit).all()
    return [ItemResponse.from_orm(item) for item in items]
