import os
import time

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.api import api_router
from app.db.database import SessionLocal,engine
from app import models

os.environ["TZ"] = settings.TIMEZONE
time.tzset()

models.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        debug=settings.DEBUG,
        openapi_url=settings.OPENAPI_URL
    )
    return application


app = get_application()



app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)