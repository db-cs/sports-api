from fastapi import FastAPI
from typing import Optional
from enum import Enum
import csv
import datetime

data = [
    {"season": 0, "results": "win", "sport": "soccer"},
    {"season": 1, "results": "lose", "sport": "football"},
    {"season": 2, "results": "win", "sport": "basketball"},
    {"season": 3, "results": "lose", "sport": "vollyball"},
]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world!"}


class Seasons(Enum):
    WINTER = 0
    SUMMER = 1
    SPRING = 2
    FALL = 3


#used to call the season Function
@app.get("/season")
async def get_season(limit: int = 10, season: int = 0):
    output = []
    for result in data:
        if result["season"] == season:
            output.append(result)
    return {"limit": limit, "season": (season, Seasons(season).name), "results": output}

# Define an Enum for the different sports
class Sports(Enum):
    SOCCER = "soccer"
    FOOTBALL = "football"
    BASKETBALL = "basketball"
    VOLLYBALL = "vollyball"

# Define the get_sport function
@app.get("/sport")
async def get_sport(sport: Sports, limit: int = 10):
    output = []
    for result in data:
        if result["sport"] == sport.value:
            output.append(result)
    return {"limit": limit, "results": output[:limit]}

results = get_sport(Sports.SOCCER, 5)