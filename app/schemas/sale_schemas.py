from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class SaleSchema(BaseModel):
    qty: int
    product_id: UUID
    users_id: UUID

    class Config:
        orm_mode = True


class SaleUpdate(SaleSchema):
    id: UUID


class SaleResponse(SaleUpdate):
    sale_at: datetime
