# Data Structures and Algorithms: Tests for PrinterClass
# 02.04.16
# @totallygloria


import unittest
from PrinterClass import Printer

class PrinterTester(unittest.TestCase):

    def test_init(self):
        # Create a printer, check if initial values match
        inkjet = Printer(6)
        self.assertEqual(inkjet.pagerate, 6)
        self.assertEqual(inkjet.currenttask, None)
        self.assertEqual(inkjet.timeremaining, 0)

    def test_tick(self):
        # Create a new printer, give it a task, check if ticking down to 0 works
        laserjet = Printer(20)
        laserjet.currenttask = True
        laserjet.timeremaining = 10
        self.assertEqual(laserjet.timeremaining, 10)
        laserjet.tick()
        self.assertEqual(laserjet.timeremaining, 9)
        for i in range(9):
            laserjet.tick()
        self.assertEqual(laserjet.currenttask, None)
        self.assertEqual(laserjet.timeremaining, 0)

    def test_busy(self):
        # Create a printer, give it a task, check if busy
        canon = Printer(12)
        self.assertEqual(canon.busy(), False)
        canon.currenttask = True
        self.assertEqual(canon.busy(), True)


if __name__ == '__main__':
    unittest.main()