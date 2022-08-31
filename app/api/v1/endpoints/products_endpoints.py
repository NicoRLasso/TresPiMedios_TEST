from typing import List
from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader

from app.services.product_services import ProductServices
from app.schemas.product_schemas import ProductResponse, ProductSchema
from app.db.database import db
from app.utils import is_admin_user

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product(new_product: ProductSchema, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        products = ProductServices(db_session)
        return products.create_product(new_product)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@router.get("/", response_model=List[ProductResponse])
def list_products(db_session=Depends(db)):
    products = ProductServices(db_session)
    return products.list_products()
