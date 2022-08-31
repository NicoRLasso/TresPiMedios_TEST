from typing import List
from app.models.products import Products
from app.services.app_service import AppService
from app.schemas.product_schemas import ProductSchema


class ProductServices(AppService):

    def __init__(self, db_session):
        super().__init__(db_session)

    def create_product(self, new_product: ProductSchema) -> Products:
        new_product = Products(
            **new_product.dict()
        )
        self.db_session.add(new_product)
        self.db_session.commit()
        return new_product

    def list_products(self) -> List[Products]:
        return self.db_session.query(Products).all()
