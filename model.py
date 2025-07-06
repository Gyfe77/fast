from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int

class CatsInput(BaseModel):
    num: int