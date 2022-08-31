from doctest import debug_script
from uuid import UUID
from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: str
    price: int

    class Config:
        orm_mode = True


class ProductResponse(ProductSchema):
    id: UUID
