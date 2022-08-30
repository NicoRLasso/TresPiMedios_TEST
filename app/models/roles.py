import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer

from app.db.database import Base


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, nullable=False)
    name = Column(String(length=30), nullable=False)
