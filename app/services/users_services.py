from uuid import UUID
from sqlalchemy.orm import Session
from app.models.roles import Roles

from app.models.users import Users
from app.schemas.user_schemas import UserSchema, RoleSchema


class UserServices:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_user(self, new_user_input: UserSchema):
        new_user = Users(
            **new_user_input.dict()
        )
        self.db_session.add(new_user)
        self.db_session.commit()

    def create_role(self, new_role_input: RoleSchema):
        new_role = Roles(
            **new_role_input.dict()
        )
        self.db_session.add(new_role)
        self.db_session.commit()

    def assign_role_to_user(self, user_id: UUID, role_id: UUID):
        user = self.db_session.query(Users).filter(Users.id == user_id).first()
        user.role_id = role_id
        self.db_session.commit()

    def lists_user(self):
        return self.db_session.query(Users).all()

    def lists_roles(self):
        return self.db_session.query(Roles).all()

    def delete_user(self, user_id: UUID):
        self.db_session.query(Users).filter(Users.id == user_id).delete()
        self.db_session.commit()
        return "Done"
