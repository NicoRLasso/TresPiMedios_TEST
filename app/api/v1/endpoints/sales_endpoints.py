from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader

from app.services.sale_services import SaleServices
from app.schemas.sale_schemas import SaleSchema, SaleResponse, SaleUpdate
from app.db.database import db
from app.utils import is_admin_user

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
def update_sale(update_sale: SaleUpdate, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        sales = SaleServices(db_session)
        return sales.update_sale(update_sale)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@router.delete("/")
def delete_sale(sale_uuid: UUID, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        sale = SaleServices(db_session)
        return sale.delete_sale(sale_uuid)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
