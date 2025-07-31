import pandas
import pydantic

class task(pydantic.BaseModel):
    def __init__(self, name: str, discription: str, priority: int):
        self.name = name
        self.discription = discription
        self.priority = priority
