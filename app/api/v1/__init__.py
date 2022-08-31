from fastapi import APIRouter
from app.api.v1.endpoints import users_endpoint
from app.api.v1.endpoints import products_endpoints
from app.api.v1.endpoints import sales_endpoints
from app.api.v1.endpoints import statistics_endpoints


api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(
    users_endpoint.router, prefix="/users", tags=["users"])
api_v1_router.include_router(
    products_endpoints.router, prefix="/products", tags=["products"])
api_v1_router.include_router(
    sales_endpoints.router, prefix="/sales", tags=["sales"])
api_v1_router.include_router(
    statistics_endpoints.router, prefix="/statistics", tags=["statistics"])
