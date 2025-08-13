import pandas
import sys
from pydantic import BaseModel
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout,QHBoxLayout, QPushButton

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
        
    def save_as_csv(self):
        task_dict = [task.dict() for task in self.tasks]
        df = pandas.DataFrame(task_dict)
        df.to_csv('Lists.csv', index= False)
        
class GUI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.to_do_list = ToDoList(tasks=[])
        
        self.setWindowTitle('TO DO LIST')
        self.setGeometry(680, 300, 400, 500)
        
        #Here are three boxes to get task name, description and priority from user.
        #name
        self.name_box = QLineEdit()
        self.name_box.setPlaceholderText('Task name')
        self.name_box.setClearButtonEnabled(True)
        self.name_box.setFixedSize(390, 40)
        #dicreption
        self.description_box = QLineEdit()
        self.description_box.setPlaceholderText('Task discription')
        self.description_box.setClearButtonEnabled(True)
        self.description_box.setFixedSize(390, 200)
        #priority
        self.priority_box = QLineEdit()
        self.priority_box.setPlaceholderText('Task priority')
        self.priority_box.setFixedSize(390, 40)
        self.priority_box.setClearButtonEnabled(True)
        
        #Here are three buttons to save, delete, save as csv.
        #save
        save_button = QPushButton()
        save_button.setText('Save')
        save_button.setFixedSize(127, 35)
        save_button.clicked.connect(self.save)
        #delete
        delete_button = QPushButton()
        delete_button.setText('delete')
        delete_button.setFixedSize(126, 35)
        #save as csv
        save_as_csv_button = QPushButton()
        save_as_csv_button.setText('Save as csv')
        save_as_csv_button.setFixedSize(127, 35)
        
        #Here are vertical and horizontal layout
        #vertical
        layout_v = QVBoxLayout()
        layout_v.setSpacing(5)
        layout_v.setContentsMargins(5, 0, 0, 0)
        layout_v.addWidget(self.name_box)
        layout_v.addWidget(self.priority_box)
        layout_v.addWidget(self.description_box)
        #horizontal
        layout_h = QHBoxLayout()
        layout_h.setSpacing(2)
        layout_h.setContentsMargins(0, 0, 0, 0)
        layout_h.addWidget(save_button)
        layout_h.addWidget(delete_button)
        layout_h.addWidget(save_as_csv_button)
        
        layout_v.addLayout(layout_h)
        layout_v.addStretch()
        self.setLayout(layout_v)
        
        self.show()
        
    def save(self):
        try:
            name = self.name_box.text().strip()
            description = self.description_box.text().strip()
            priority = int(self.priority_box.text().strip())
            
            if name and priority:
                t = Task(name= name, description= description, priority= priority)
                self.to_do_list.tasks.append(t)
                self.to_do_list.show()
                
                self.name_box.clear()
                self.description_box.clear()
                self.priority_box.clear()
        except:
            print("Error: Invalid Input! Fill all the boxes and priority must be a valid integer.")
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())
