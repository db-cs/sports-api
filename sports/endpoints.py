from fastapi import APIRouter

endpoints_router = APIRouter()

#used to call Sport Function
@endpoints_router.get("/sport")
def sport():
    return {
        "Sport Result"
    }

#used to call the season Function
@endpoints_router.get("/season")
def season():
    return{
        "Season Result"
    }

