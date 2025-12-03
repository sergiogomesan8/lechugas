from pydantic import BaseModel
from datetime import date


class CreateProductDTO(BaseModel):
    name: str
    expiration_date: date
    initial_stock: int