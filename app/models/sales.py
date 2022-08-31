import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.sql.sqltypes import Date

from app.db.database import Base
from app.models.products import Products
from app.models.users import Users


class Sales(Base):
    __tablename__ = 'sales'

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, nullable=False)
    qty = Column(Integer, nullable=False)
    sale_at = Column(Date, default=datetime.utcnow)
    products_id = Column(UUID(as_uuid=True), ForeignKey(
        Products.id), nullable=False)
    users_id = Column(UUID(as_uuid=True), ForeignKey(Users.id), nullable=False)
