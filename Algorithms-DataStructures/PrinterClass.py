# Data Structures and Algorithms: Printer Queue Simulation - PrinterClass
# 02.04.16
# @totallygloria


"""
The Printer class will need to track whether it has a current task.
If it does, then it is busy and the amount of time needed can be computed
from the number of pages in the task. The constructor will also allow the pages-per-minute
setting to be initialized. The tick method decrements the internal timer and sets the
printer to idle if the task is completed.
"""


class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currenttask = None
        self.timeremaining = 0

    def tick(self):
        if self.currenttask:
            self.timeremaining -= 1
            if self.timeremaining <= 0:
                self.currenttask = None

    def busy(self):
        if self.currenttask:
            return True
        return False

    def startnext(self, newtask):
        self.currenttask = newtask
        self.timeremaining = newtask.getpages() * 60 / self.pagerate
