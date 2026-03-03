from pydantic import BaseModel
from typing import Optional

from models import Item

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemResponse(Item):
    pass
