from uuid import UUID
from pydantic import BaseModel


class UserSchema(BaseModel):
    document: str
    last_name: str
    name: str

    class Config:
        orm_mode = True


class UserResponse(UserSchema):
    id: UUID


class UserRoleResponse(UserResponse):
    roles_id: UUID


class RoleSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RoleResponse(RoleSchema):
    id: UUID
