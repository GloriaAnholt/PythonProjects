# Data Structures and Algorithms: Printer Queue Simulation - TaskClass
# 02.09.16
# @totallygloria


"""
The Task class will represent a single printing task. When the task is created,
a random number generator will provide a length from 1 to 20 pages. We have chosen to
use the randrange function from the random module.

Each task will also need to keep a timestamp to be used for computing waiting time.
This timestamp will represent the time that the task was created and placed in the printer queue.
The waitTime method can then be used to retrieve the amount of time spent in the queue before
printing begins.

"""

from random import randrange


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = randrange(1, 21)

    def getstamp(self):
        return self.timestamp

    def getpages(self):
        return self.pages

    def waittime(self, currenttime):
        return currenttime - self.timestamp
