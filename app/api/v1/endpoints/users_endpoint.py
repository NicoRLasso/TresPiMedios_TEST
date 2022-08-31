from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader

from app.services.user_services import UserServices
from app.schemas.user_schemas import UserResponse, UserSchema, RoleResponse, RoleSchema
from app.db.database import db
from app.utils import is_admin_user

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(new_user: UserSchema, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.create_user(new_user)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@ router.post("/roles", response_model=RoleResponse)
def assign_role_to_user(user_id: UUID, role_id: UUID, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.assign_role_to_user(user_id, role_id)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@ router.post("/roles", response_model=RoleResponse)
def create_roles(new_role: RoleResponse, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.create_role(new_role)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@ router.get("/", response_model=List[UserResponse])
def list_users(db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.lists_user()
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@ router.get("/roles", response_model=List[RoleResponse], api_key=Security(APIKeyHeader(name="Auth")))
def list_roles(db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.lists_roles()
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@ router.delete("/")
def delete_user(user_id: UUID, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        user = UserServices(db_session)
        return user.delete_user(user_id)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
