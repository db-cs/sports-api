from pydantic import BaseModel

class Result(BaseModel):
    type: str
    description: str

class GameNotes(BaseModel):
    type: str
    description: str

class Link(BaseModel):
    type: str
    description: str

class OurScore(BaseModel):
    type: int
    description: int

class TheirScore(BaseModel):
    type: int
    description: int

class Team(BaseModel):
    type: enumerate
    description: enumerate

class Sport(BaseModel):
    type: enumerate
    description: enumerate

class Season(BaseModel):
    type: enumerate
    description: enumerate

class Date(BaseModel):
    type: str
    description: str

class Opponents(BaseModel):
    type: str
    description: str

class Location(BaseModel):
    type: str
    description: str

class Identification(BaseModel):
    type: str
    description: str