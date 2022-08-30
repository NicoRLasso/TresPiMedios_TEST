from uuid import UUID
from fastapi import APIRouter, Depends, Security
from starlette import status

from app.models.users import Users
from app.services.users_services import UserServices
from app.schemas.user_schemas import UserResponse, UserSchema, RoleResponse, RoleSchema
from app.db.database import db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(new_user: UserSchema, db_session=Depends(db)):
    user = UserServices(db_session)
    return user.create_user(new_user)


@router.post("/roles", response_model=RoleResponse)
def assign_role_to_user(user_id: UUID, role_id: UUID, db_session=Depends(db)):
    user = UserServices(db_session)
    return user.assign_role_to_user(user_id, role_id)


@router.post("/roles", response_model=RoleResponse)
def create_roles(new_role: RoleResponse, db_session=Depends(db)):
    user = UserServices(db_session)
    return user.create_role(new_role)


@router.get("/", response_model=UserResponse)
def list_users(db_session=Depends(db)):
    user = UserServices(db_session)
    return user.lists_user()


@router.get("/roles", response_model=UserResponse)
def list_roles(db_session=Depends(db)):
    user = UserServices(db_session)
    return user.lists_roles()


@router.delete("/")
def delete_user(user_id: UUID, db_session=Depends(db)):
    user = UserServices(db_session)
    return user.delete_user(user_id)
