# To Do List Application

## Overview
This is a simple command-line To Do List application written in Python. It allows users to manage tasks with names, descriptions, and priorities, save them to a CSV file, and display them sorted by priority.

## Features
- Create tasks with name, description, and priority
- Delete tasks by name
- Display tasks sorted by priority
- Save tasks to a CSV file (`Lists.csv`)

## Project Structure
- `To_do_list.py`: Contains the `Task` and `ToDoList` classes
- `test_case.py`: Unit tests for the ToDoList functionality
- `Lists.csv`: Generated CSV file storing tasks
- `requirements.txt`: Lists required Python packages

## Installation
1. Clone or download the project files.
2. Ensure Python 3.8+ is installed.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Import and use the `To Do List` class in a Python script:
   ```python
   from To_do_list import Task, ToDoList

   tasks = [
       Task(name="Task1", description="First task", priority=2),
       Task(name="Task2", description="Second task", priority=1)
   ]
   todo = ToDoList(tasks)
   todo.show()           # Display tasks
   todo.delete("Task1")  # Delete a task
   todo.save_to_csv()    # Save to Lists.csv
   ```
2. Run tests:
   ```bash
   python -m unittest test_todolist.py
   ```

## Running Tests
The test suite (`test_case.py`) verifies the functionality of task deletion, sorting, and CSV saving. Run tests using the command above.

## Dependencies
See `requirements.txt` for required packages.

## Notes
- The CSV file (`Lists.csv`) is created in the project directory when `save_to_csv()` is called.
- Tasks are sorted by priority (ascending) when displayed.
