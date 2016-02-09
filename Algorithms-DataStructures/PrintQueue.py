# Data Structures and Algorithms: Printer Queue Simulation - PrintQueue
# 02.09.16
# @totallygloria

"""
The printQueue object is an instance of our existing queue ADT.
A boolean helper function, newPrintTask, decides whether a new printing task has been
created. We have again chosen to use the randrange function from the random module to
return a random integer between 1 and 180. Print tasks arrive once every 180 seconds.
By arbitrarily choosing 180 from the range of random integers, we can simulate this
random event. The simulation function allows us to set the total time and the pages
per minute for the printer.
"""

from random import randrange
from QueueClass import Queue
from PrinterClass import Printer
from TaskClass import Task


def simulation(numseconds, pagesperminute):
    labprinter = Printer(pagesperminute)
    printerqueue = Queue()
    waitingtimes = []
    longestqueue = 0

    for currentsecond in range(numseconds):

        if newprinttask():
            newtask = Task(currentsecond)
            printerqueue.enqueue(newtask)
            if printerqueue.size() > longestqueue:
                longestqueue = printerqueue.size()

        if not labprinter.busy() and printerqueue.has_items():
            nexttask = printerqueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentsecond))
            labprinter.startnext(nexttask)

        labprinter.tick()

    averagewait = sum(waitingtimes)/len(waitingtimes)
    print "Average Wait %6.2f secs %3d tasks remaining." % (averagewait, printerqueue.size())
    print "The longest the queue got to was %d tasks. \n" % (longestqueue)


def newprinttask():
    createtask = randrange(1, 181)
    if createtask == 180:
        return True
    return False


for i in range(10):
    simulation(3600, 5)


