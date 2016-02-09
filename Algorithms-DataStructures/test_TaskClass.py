# Data Structures and Algorithms: Printer Queue Simulation - TaskClass
# 02.09.16
# @totallygloria

import unittest

from TaskClass import Task


class TaskTester(unittest.TestCase):

    def test_task(self):
        task = Task(10)
        self.assertEqual(task.timestamp, 10, msg='timestamp correct')
        self.assertGreater(task.pages, 0, msg='greater than zero passes')
        self.assertLess(task.pages, 21, msg='less than 21 passes')
        self.assertEqual(task.pages, task.getpages())
        self.assertEqual(task.getstamp(), 10)
        self.assertEqual(task.waittime(10), 0)
        self.assertEqual(task.waittime(1), -9)
        self.assertEqual(task.waittime(100), 90)

if __name__ == '__main__':
    unittest.main()
