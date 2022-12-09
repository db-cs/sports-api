from fastapi import APIRouter

endpoints_router = APIRouter()
from sports import *
 
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
        "data": data[:limit], season:[season]
    }

