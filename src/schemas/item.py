from pydantic import BaseModel
from typing import Optional

# Shared properties
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass

# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass

# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    owner_id: int

    model_config = {"from_attributes": True}

# Properties to return to client
class Item(ItemInDBBase):
    pass
