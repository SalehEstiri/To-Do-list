import unittest
import pandas as pd
import os
from To_do_list import Task, ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.task1 = Task(name="Buy bread", description="I don't know", priority=2)
        self.task2 = Task(name="Homework", description="Do your homework", priority=1)
        self.task3 = Task(name="Exam", description="Prepare for your exam", priority=3)
        self.to_do_list = ToDoList([self.task1, self.task2, self.task3])

    def test_delete(self):
        self.to_do_list.delete("Buy bread")
        self.assertEqual(len(self.to_do_list.tasks), 2)
        self.assertNotIn("Buy bread", [task.name for task in self.to_do_list.tasks])
