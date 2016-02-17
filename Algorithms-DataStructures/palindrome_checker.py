# Data Structures and Algorithms: Palindrome Checker
# 02.17.16
# @totallygloria


from DequeClass import Deque


def user_input():
    # Separates the raw input from the primary check
    print "Enter a word to see if it's the same front-to-back as back-to-front."
    word = raw_input("> ")
    if len(word) <= 2:
        print "A palindrome needs three or more letters."
        user_input()
    return word


def build_deque(word):
    # creates the deque, maintains letter order
    d = Deque()
    for letter in word:
        d.addrear(letter)

    return d


def pal_checker(deque):
    # pops front and back, returns true or false
    match = True
    if (deque.size % 2) == 0:
        for i in range(deque.size):
            f = deque.removefront()
            r = deque.removerear()
            if f != r:
                match = False
                break
    else:
        for i in range(deque.size - 1):
            f = deque.removefront()
            r = deque.removerear()
            if f != r:
                match = False
                break

    return match



def main():
    # gets input, builds a deque, checks if matches, repeats
    print "This is a palindrome checker."
    repeat = True

    while repeat:
        word = user_input()
        build_deque(word)
