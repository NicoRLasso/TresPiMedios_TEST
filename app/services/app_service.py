from sqlalchemy.orm import Session


class DBSessionMixin:
    def __init__(self, db_session: Session):
        self.db_session = db_session


class AppService(DBSessionMixin):
    pass
