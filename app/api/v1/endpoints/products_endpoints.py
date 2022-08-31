from typing import List
from fastapi import APIRouter, Depends

from app.services.product_services import ProductServices
from app.schemas.product_schemas import ProductResponse, ProductSchema
from app.db.database import db

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product(new_product: ProductSchema, db_session=Depends(db)):
    products = ProductServices(db_session)
    return products.create_product(new_product)


@router.get("/", response_model=List[ProductResponse])
def list_products(db_session=Depends(db)):
    products = ProductServices(db_session)
    return products.list_products()
