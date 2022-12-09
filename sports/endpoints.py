from fastapi import APIRouter
from .database.databases import data

endpoints_router = APIRouter()

#used to call Sport Function
@endpoints_router.get("/sport")
def sport():
    return {
        "Sport Result"
    }

#used to call the season Function
@endpoints_router.get("/season")
def season(limit: int = 10):
    return {
        "limit": limit,
        "data": data[:limit],
    }

@endpoints_router.get("/win/")
def win():
    return (data)