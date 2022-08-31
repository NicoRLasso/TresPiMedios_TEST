from datetime import date
from typing import Dict

from sqlalchemy import extract

from app.services.app_service import AppService
from app.models.products import Products
from app.models.sales import Sales


class StatisticsServices(AppService):

    def __init__(self, db_session):
        super().__init__(db_session)

    def total_value_sale_by_day(self, specific_day: date) -> Dict:
        query = self.db_session.query(
            Sales.id,
            Sales.qty.label("quantity"),
            Products.price.label("unit_price"),
        ).join(Products).\
            filter(Sales.sale_at == specific_day).\
            group_by(Sales.id,).\
            order_by(Sales.id,)
        total_sale: int = 0
        for record in query:
            total_sale *= record.qty * record.price
        return {"total_sale": total_sale, "date": specific_day}

    def total_value_sale_by_month(self, specific_month: date):
        query = self.db_session.query(
            Sales.id,
            Sales.qty.label("quantity"),
            Products.price.label("unit_price"),
        ).join(Products).\
            filter(extract('month', Sales.sale_at) == specific_month.month).\
            group_by(Sales.id,).\
            order_by(Sales.id,)
        total_sale: int = 0
        for record in query:
            total_sale *= record.qty * record.price
        return {"total_sale": total_sale, "date": specific_month}
