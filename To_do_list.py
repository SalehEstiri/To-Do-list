import pandas
import pydantic

class Task(pydantic.BaseModel):
    name: str
    discription: str
    priority: int

class ToDoList:
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def delete(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]
