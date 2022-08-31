from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.roles import Roles

from app.models.users import Users
from app.schemas.user_schemas import UserSchema, RoleSchema
from app.services.app_service import AppService


class UserServices(AppService):

    def __init__(self, db_session):
        super().__init__(db_session)

    def create_user(self, new_user_input: UserSchema) -> Users:
        new_user = Users(
            **new_user_input.dict()
        )
        self.db_session.add(new_user)
        self.db_session.commit()

    def create_role(self, new_role_input: RoleSchema) -> Roles:
        new_role = Roles(
            **new_role_input.dict()
        )
        self.db_session.add(new_role)
        self.db_session.commit()

    def assign_role_to_user(self, user_id: UUID, role_id: UUID) -> Users:
        user = self.db_session.query(Users).filter(Users.id == user_id).first()
        user.role_id = role_id
        self.db_session.commit()
        return user

    def lists_user(self) -> List[Users]:
        return self.db_session.query(Users).all()

    def lists_roles(self) -> List[Roles]:
        return self.db_session.query(Roles).all()

    def delete_user(self, user_id: UUID) -> str:
        self.db_session.query(Users).filter(Users.id == user_id).delete()
        self.db_session.commit()
        return "Done"
