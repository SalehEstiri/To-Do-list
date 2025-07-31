import pandas
import pydantic

class task(pydantic.BaseModel):
    name: str
    discription: str
    priority: int

class ToDoList(task):
    def __init__(self, tasks: list[task]):
        self.tasks = tasks

    def delete(self, name):
        self.tasks.remove(name)