import pandas
from pydantic import BaseModel
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton

class Task(BaseModel):
    name: str
    description: str
    priority: int

class ToDoList:
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def delete(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def show(self):
        #Sorting the tasks by their priority
        self.tasks.sort(key= lambda task: task.priority)
        for task in self.tasks:
            print('-------------------------')
            print(f'{task.priority}- {task.name}')
            print(task.description)
            print('-------------------------')
        
    def save_to_csv(self):
        task_dict = [task.dict() for task in self.tasks]
        df = pandas.DataFrame(task_dict)
        df.to_csv('Lists.csv', index= False)
