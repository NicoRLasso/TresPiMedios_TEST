from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Security
from starlette import status

from app.services.sale_services import SaleServices
from app.schemas.sale_schemas import SaleSchema, SaleResponse, SaleUpdate
from app.db.database import db

router = APIRouter()


@router.post("/", response_model=SaleResponse)
def create_sale(new_sale: SaleSchema, db_session=Depends(db)):
    sales = SaleServices(db_session)
    return sales.create_sale(new_sale)


@router.get("/", response_model=List[SaleResponse])
def list_sales(db_session=Depends(db)):
    sales = SaleServices(db_session)
    return sales.lists_sales()


@router.post("/", response_model=SaleResponse)
def update_sale(update_sale: SaleUpdate, db_session=Depends(db)):
    sales = SaleServices(db_session)
    return sales.update_sale(update_sale)


@router.delete("/")
def delete_sale(sale_uuid: UUID, db_session=Depends(db)):
    sale = SaleServices(db_session)
    return sale.delete_sale(sale_uuid)
