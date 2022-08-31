from datetime import date
from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader

from app.services.statistics_services import StatisticsServices
from app.db.database import db
from app.utils import is_admin_user

router = APIRouter()


@router.post("/daily_total_sale")
def daily_total_sale(date: date, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        statistic = StatisticsServices(db_session)
        return statistic.total_value_sale_by_day(date)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@router.post("/monthly_total_sale")
def monthly_total_sale(date: date, db_session=Depends(db), api_key=Security(APIKeyHeader(name="Auth"))):
    if is_admin_user(api_key, db_session):
        statistic = StatisticsServices(db_session)
        return statistic.total_value_sale_by_month(date)
    else:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
