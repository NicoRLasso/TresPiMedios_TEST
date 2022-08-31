from email.policy import default
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey

from app.db.database import Base
from app.models.roles import Roles


class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, nullable=False)
    name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    document = Column(String(length=30), nullable=False)
    roles_id = Column(UUID(as_uuid=True), ForeignKey(Roles.id), nullable=False)
