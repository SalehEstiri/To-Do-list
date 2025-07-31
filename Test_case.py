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

    def test_show(self):
        self.to_do_list.show()
        self.assertEqual(self.to_do_list.tasks[0].name, "Homework")
        self.assertEqual(self.to_do_list.tasks[1].name, "Buy bread")
        self.assertEqual(self.to_do_list.tasks[2].name, "Exam")
      
    def test_save_to_csv(self):
        self.to_do_list.save_to_csv()
        self.assertTrue(os.path.exists('Lists.csv'))
        
        df = pd.read_csv('Lists.csv')
        self.assertEqual(len(df), 3)
        self.assertEqual(list(df.columns), ['name', 'description', 'priority'])
        self.assertTrue("Task1" in df['name'].values)
        self.assertTrue("First task" in df['description'].values)
        
    def remove_csv(self):
        if os.path.exists('Lists.csv'):
            os.remove('Lists.csv')


if __name__ == '__main__':
    unittest.main()
