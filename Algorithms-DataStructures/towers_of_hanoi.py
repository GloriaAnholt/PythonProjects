# Algorithms & data Structures: Recursion - Towers of Hanoi
# 3/16/16
# @totallygloria


import random


def user_input():

    num_disks = int(raw_input('Enter a number of disks to move, between 1 and 10: '))
    while (num_disks <= 0) or (num_disks >= 11):
        num_disks = int(raw_input('Please enter a number of disks to move, between 1 and 10: '))

    locations = [1, 2, 3]

    start_loc = int(raw_input('Enter a starting pole (1, 2, or 3): '))
    if start_loc not in locations:
        start_loc = random.randrange(1,3)
        print "Invalid input, starting on ", start_loc
    locations.remove(start_loc)

    dest_loc = int(raw_input('Enter the destination pole (must be different from the start): '))
    if dest_loc == start_loc:
        dest_loc = random.choice(locations)
        print "Invalid distination, starting on ", dest_loc
    locations.remove(dest_loc)

    helper = locations.pop()

    return num_disks, start_loc, dest_loc, helper


def game_setup():

    poles = []
    start_loc = []
    dest_loc = []
    help_loc = []

    num_disks, start, dest, helper = user_input()

    for i in range(num_disks,0, -1):
        start_loc.append(i)

    if start == 1:
        poles.append(start_loc)
    elif dest == 1:
        poles.append(dest_loc)
    elif helper == 1:
        poles.append(help_loc)

    if start == 2:
        poles.append(start_loc)
    elif dest == 2:
        poles.append(dest_loc)
    elif helper == 2:
        poles.append(help_loc)

    if start == 3:
        poles.append(start_loc)
    elif dest == 3:
        poles.append(dest_loc)
    elif helper == 3:
        poles.append(help_loc)

    return num_disks, poles



'''
def draw_game(num_disks, start_loc):

    start_peg = []

    for i in range(num_disks, 0, -1):
        start_peg.append("disk"+str(i))

    if start_loc == 1:
        for i in range(num_disks-1, -1, -1):
            print start_peg[i], "\t\t", "|", "\t\t", "|"
    elif start_loc == 2:
        for i in range(num_disks-1, -1, -1):
            print "|", "\t\t", start_peg[i], "\t\t", "|"
    elif start_loc == 3:
        for i in range(num_disks-1, -1, -1):
            print "|", "\t\t", "|", "\t\t", start_peg[i]
'''


def move_disk(current_loc, dest_loc):
    """ The idea is that this would pop a disk off it's current location
    and then append it to the correct list.
    """
    current_disk = current_loc[-1]
    print "moving disk number %s from pole %s to pole %s" % (current_disk, current_loc, dest_loc)
    current_disk = current_loc.pop()
    dest_loc.append(current_disk)
    return current_loc, dest_loc


def hanoi_solver(num_disks, from_loc, dest_loc, helper_loc):
    """ If the number of disks is one, just move it to the destination.
    Else, move the (n-1) stack to the helper, move the disk to the dest, move
    the stack to the dest-peg. The first and third calls are recursive, the middle
    is simply a call to the move function.
    """

    if num_disks == 1:
        move_disk(from_loc, dest_loc)
    elif num_disks >=1:
        hanoi_solver(num_disks - 1, from_loc, helper_loc, dest_loc)
        move_disk(from_loc, dest_loc)
        hanoi_solver(num_disks - 1, helper_loc, dest_loc, from_loc)



def main():

    num_disks, poles = game_setup()
    hanoi_solver(num_disks, start_loc, dest_loc, helper)




if __name__ == '__main__':
    main()
