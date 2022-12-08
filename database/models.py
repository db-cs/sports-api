

from pydantic import BaseModel
from enum import Enum

class Season(Enum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    FALL = 3

class Team(Enum):
    JV = 0
    VARSITY = 1
    FRESHMAN = 2

class Sport(Enum):
    M_BASKETBALL = 0 
    W_BASKETBALL = 1 
    BOWLING = 2
    M_CROSS_COUNTRY = 3
    W_CROSS_COUNTRY = 4
    FOOTBALL = 5
    M_GOLF = 6
    W_GOLF = 7
    W_SOCCER = 8
    W_VOLLEYBALL = 9

class Result(BaseModel):
    our_score: int
    their_score: int
    game_notes: str
    result: str
    link: str
    season: Season
    team: Team
    sport: Sport
