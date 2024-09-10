from fastapi import APIRouter

from .personal_data import personal_data_router


all_routers = APIRouter()
all_routers.include_router(personal_data_router)

__all__ = ["all_routers"]
