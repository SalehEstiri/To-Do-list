import pandas
import sys
from pydantic import BaseModel
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt6.QtCore import QSize

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
        
class GUI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('TO DO LIST')
        self.setGeometry(680, 360, 400, 500)
        
        #Here are three boxes to get task name, discreption and priority from user.
        #name
        name_box = QLineEdit()
        name_box.setPlaceholderText('Task name')
        name_box.setClearButtonEnabled(True)
        name_box.setFixedSize(QSize(390, 50))
        #dicreption
        discreption_box = QLineEdit()
        discreption_box.setPlaceholderText('Task discription')
        discreption_box.setClearButtonEnabled(True)
        discreption_box.setFixedSize(QSize(390, 50))
        #priority
        priority_box = QLineEdit()
        priority_box.setPlaceholderText('Task priority')
        priority_box.setFixedSize(QSize(390, 200))
        priority_box.setClearButtonEnabled(True)
        
        layout = QVBoxLayout()
        layout.addWidget(name_box)
        layout.addWidget(discreption_box)
        layout.addWidget(priority_box)
        self.setLayout(layout)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())
