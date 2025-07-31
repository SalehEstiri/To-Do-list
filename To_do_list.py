import pandas
import pydantic

class Task(pydantic.BaseModel):
    name: str
    discription: str
    priority: int

class ToDoList(Task):
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def delete(self, name):
        self.tasks.remove(name)