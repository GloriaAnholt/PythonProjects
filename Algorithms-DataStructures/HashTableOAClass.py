# Algorithms and Data Structures: Hash Tables & Hashing
# 4.26.2016
# @totallygloria

"""
Uses a python list to hold the values in the hash table.
Hashing function is a separate call, so it can be changed independently.
If there's a collision, resolves using open addressing.
"""
from calculate_two_off_primes import massage_primes


class OAHashTable(object):

    def __init__(self):
        self.size = 0
        self.occupancy = 0
        self.__htable = []
        self.initialize_table()

    def initialize_table(self):
        """ Asks the user for the approximate table size they want, this only happens on the
        first creation of a table. If input is invalid, set the table to smallest pair prime (5).
        Otherwise, call the resize_hash function to deal with sizing logic."""
        try:
            des_len = int(raw_input('Approximately how large would you like your initial table to be?'))
        except ValueError:
            self.size = 5
            self.__htable = [None] * 5
            return
        else:
            self.resize_table(des_len)

    def resize_table(self, des_len):
        """ Sets self.htable to a prime-length list, up to a max length of 104683. The prime
        selected is the first prime number larger than the desired length, where there also
        exists a pair prime number exactly 2 smaller than the table size (for rehashing).
        If it's the first creation of the table, fills the list with Nones; if it's a resizing
        of the table, rehashes every single entry and reinserts them. """
        two_off_primes = massage_primes()
        largest_prime = two_off_primes[-1]
        # If this is the first time making the table, populate with Nones
        if self.occupancy == 0:
            if des_len > largest_prime:
                print "Largest available prime is %d, setting as max table size." % largest_prime
                self.size = largest_prime
                self.__htable = [None] * largest_prime
            else:
                i = 0
                while des_len > two_off_primes[i]:
                    i += 1
                self.size = two_off_primes[i]
                self.__htable = [None] * two_off_primes[i]
        # Otherwise, this is a resizing up, and we need to rehash every member
        # Makes a new table, fills with old tables items, then moves pointer to the new table
        else:
            if des_len > largest_prime:
                self.size = largest_prime
                new_table = [None] * largest_prime
            else:
                i = 0
                while des_len > two_off_primes[i]:
                    i += 1
                self.size = two_off_primes[i]
                new_table = [None] * two_off_primes[i]

            for entry in self.__htable:
                if entry == 'USED' or entry == None:
                    pass
                else:
                    hashedval = self.compute_hash(entry[0])
                    new_table[hashedval] = (entry[0], entry[1])
            self.__htable = new_table
            return

    def compute_hash(self, item):
        """ Given a item, returns its hashed value """
        # TODO this needs a recompute for collisions, I think
        hashedval = item ** 2
        return hashedval % self.size

    def insert_hash(self, key, value):
        """ Hashes item, if the slot is empty it inserts, otherwise it walks the table
        until it finds an open slot (None) or a 'USED' slot and puts it there.
        Wraps at the end of the table. Does not accept duplicate entries. """

        if (float(self.occupancy) / float(self.size)) >= .70:
            self.resize_table(self.size * 2)

        hashed_val = self.compute_hash(key)

        while self.__htable[hashed_val] is not None and self.__htable[hashed_val] != 'USED':
            if isinstance(self.__htable[hashed_val], tuple) and self.__htable[hashed_val][0] == key:
                return
            hashed_val += 1
            if hashed_val >= self.size:
                hashed_val = 0

        self.__htable[hashed_val] = (key, value)
        self.occupancy += 1

    def search_hash(self, key):
        """ Hashes item, checks if it's in the hash table - if it's not where it's expected
        to be, walks the table until a None is found. Returns a boolean. """
        # TODO: Should searching a hash for a key return the value?
        hashed_val = self.compute_hash(key)

        if isinstance(self.__htable[hashed_val], tuple) and self.__htable[hashed_val][0] == key:
            return True
        else:
            if self.__htable[hashed_val] is not None:
                while self.__htable[hashed_val] is not None:
                    hashed_val += 1
                    if hashed_val >= self.size:
                        hashed_val = 0
                    if isinstance(self.__htable[hashed_val], tuple) and self.__htable[hashed_val][0] == key:
                        return True
            return False

    def remove_item(self, key):
        """ Searches for a key in the hash table, if it's not in the proper slot,
        checks until you hit the first None. When the key is found, it's replaced
        with a USED marker and returns a boolean. """
        hashed_val = self.compute_hash(key)
        if self.__htable[hashed_val][0] == key:
            self.__htable[hashed_val] = 'USED'
            self.occupancy -= 1
            return True
        else:
            if self.__htable[hashed_val][0] != key and self.__htable[hashed_val] is not None:
                while self.__htable[hashed_val] is not None:
                    if self.__htable[hashed_val][0] == key:
                        self.__htable[hashed_val] = 'USED'
                        self.occupancy -= 1
                        return True
                    hashed_val += 1
                    if hashed_val >= self.size:
                        hashed_val = 0
            return False
