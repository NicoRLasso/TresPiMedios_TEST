from typing import List
from app.models.sales import Sales
from app.services.app_service import AppService
from app.schemas.sale_schemas import SaleSchema, SaleUpdate


class SaleServices(AppService):

    def __init__(self, db_session):
        super().__init__(db_session)

    def create_sale(self, new_sale_input: SaleSchema) -> Sales:
        new_sale = Sales(
            **new_sale_input.dict()
        )
        self.db_session.add(new_sale)
        self.db_session.commit()
        return new_sale

    def update_sale(self, sale_update: SaleUpdate) -> Sales:
        updated_sale: Sales = self.db_session.query(
            Sales).filter(Sales.id == sale_update.id).first()
        updated_sale.products_id = sale_update.products_id
        updated_sale.qty = sale_update.qty
        return updated_sale

    def lists_sales(self) -> List[Sales]:
        return self.db_session.query(Sales).all()

    def delete_sale(self, sale_id) -> str:
        self.db_session.query(Sales).filter(Sales.id == sale_id).delete()
        self.db_session.commit()
        return "Done"
