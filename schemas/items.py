from typing import Union, Optional

from fastapi import Path
from pydantic import BaseModel


class Item(BaseModel):
    name: str = Path(
        min_length=3,
        max_length=64,
        title="Item's name",
    )
    description: Union[str, None] = None
    price: float
    tax: Optional[int]
    secret: str


class ItemOut(BaseModel):
    name: str
    price: float
    car: str
