# Algorithms and Data Structures: Hash Tables & Hashing
# 4.19.2016
# @totallygloria

"""
Uses a python list to hold the values in the hash table.
Hash function is a basic module arithmetic:
   h(item) = item % table_size
If there's a collision, converts the slot to a list and appends
the new element to the list.
"""



def create_table(des_len):
    # Returns a list 2x the desired length, populated with None
    return [None] * (2 * des_len)


def insert_hash(item, table):
    # Hashes item, if the only one at a slot it inserts, otherwise converts slot
    # to a set and/or adds to existing set
    size = len(table)
    hashed_val = item % size
    if table[hashed_val] is None:
        table[hashed_val] = item
    else:
        if isinstance(table[hashed_val], set):
            table[hashed_val].add(item)
        else:
            temp = table[hashed_val]
            table[hashed_val] = set()
            table[hashed_val].add(temp)
            table[hashed_val].add(item)


def extend_hash(items, table):
    # Hashes item one at a time, if the only one at a slot it inserts,
    # otherwise converts slot to a set and/or adds to existing set
    size = len(table)
    for item in items:
        hashed_val = item % size
        if table[hashed_val] is None:
            table[hashed_val] = item
        else:
            if isinstance(table[hashed_val], set):
                table[hashed_val].add(item)
            else:
                temp = table[hashed_val]
                table[hashed_val] = set()
                table[hashed_val].add(temp)
                table[hashed_val].add(item)


def search_hash(item, table):
    # Hashes item, checks if it's in the hash table, returns a boolean.
    hashed_val = item % len(table)
    if isinstance(table[hashed_val], int) or table[hashed_val] == None:
        return table[hashed_val] == item
    else:
        for val in table[hashed_val]:
            if item == val:
                return True







