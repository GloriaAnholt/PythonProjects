# Data Structures and Algorithms: Queue
# 01.05.16
# @totallygloria

from QueueClass import Queue



def player_builder():
    print "Let's play hot potato! Please enter the names of the players, type 'DONE' when done."
    name = raw_input('> ')
    players = Queue()

    while (name != 'DONE'):
        players.enqueue(name)
        name = raw_input('> ')

    return players

def hot_potato(players):
    try:
        passes = abs(int(raw_input('How many passes should we do? Enter a number: ')))
    except ValueError:
        print "That's not a valid number, let's do 3 passes."
        passes = 3

    current = players.dequeue()

    for i in range(passes):
        players.enqueue(current)
        current = players.dequeue()

    print "%s is out!" % (current)

    if players.size() == 1:
        return players.dequeue()
    else:
        return hot_potato(players)


def main():
    players = player_builder()
    win = hot_potato(players)
    print win, "wins!"

