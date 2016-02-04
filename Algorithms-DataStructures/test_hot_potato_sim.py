# Refactoring game to accept multiple inputs. Testing first.


import sys
import unittest
from StringIO import StringIO

from hot_potato_sim import player_builder
from hot_potato_sim import hot_potato
from QueueClass import Queue

class PotatoTester(unittest.TestCase):

    def test_player_builder(self):
        test_input = StringIO("Gloria\nSchwern\nFrankie\nEric\nDONE")
        sys.stdin = test_input
        sys.stdout = StringIO()
        players = player_builder()
        self.assertEqual(players.size(), 4)

        empty_input = StringIO("DONE")
        sys.stdin = empty_input
        no_players = player_builder()
        self.assertEqual(no_players.size(), 0)

    def test_hot_potato(self):
        players = Queue()
        names = ["Gloria", "Schwern", "Frankie", "Eric"]
        for name in names:
            players.enqueue(name)
        test_input = StringIO("1\n1\n1\n")
        sys.stdin = test_input
        sys.stdout = StringIO()
        self.assertEqual(hot_potato(players), "Gloria")


if __name__ == '__main__':
    unittest.main()
