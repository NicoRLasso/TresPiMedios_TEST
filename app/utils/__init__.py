import json
import contextlib

from app.db.database import db
from app.models.products import Products
from app.models.roles import Roles
from app.models.users import Users

get_db_wrapper = contextlib.contextmanager(db)


def charge_products_fixtures():
    try:
        with get_db_wrapper() as db_session:
            file = open('app/utils/products.json')
            data = json.load(file)
            for row in data:
                new_product = Products(
                    **row
                )
                db_session.add(new_product)
            db_session.commit()
    except Exception as error:
        pass


def charge_roles_fixtures():
    try:
        with get_db_wrapper() as db_session:
            file = open('app/utils/roles.json')
            data = json.load(file)
            for row in data:
                new_product = Roles(
                    **row
                )
                db_session.add(new_product)
            db_session.commit()
    except Exception as error:
        pass


def charge_admin_fixtures():
    try:
        with get_db_wrapper() as db_session:
            new_user = Users(
                id="3fc73783-8c78-49c5-879e-d8b4d6780378",
                name="Admin",
                last_name="Admin",
                document="12345678",
                roles_id="baa38a8a-2b02-4c24-8d32-be7785061414"
            )
            db_session.add(new_user)
            db_session.commit()
    except Exception as error:
        pass


def is_admin_user(user_id, db_session) -> bool:
    try:
        user = db_session.query(Users).filter(Users.id == user_id).first()
        role = db_session.query(Roles).filter(
            Roles.id == user.roles_id).first()
        if role.name == "admin":
            return True
        return False
    except Exception as error:
        return False
