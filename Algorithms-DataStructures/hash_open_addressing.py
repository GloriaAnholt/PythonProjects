# Algorithms and Data Structures: Hash Tables & Hashing
# 4.21.2016
# @totallygloria

"""
Uses a python list to hold the values in the hash table.
Hash function is a basic module arithmetic:
   h(item) = item**2 % table_size
If there's a collision, resolves using open addressing.
"""


def create_table(des_len):
    # Returns a list 2x the desired length, populated with None
    return [None] * (2 * des_len)


def insert_hash(item, table):
    # Hashes item, if the slot is empty it inserts, otherwise it walks the table
    # until it finds and open slot and puts it there.
    size = len(table)
    hashed_val = item**2 % size
    if table[hashed_val] is None or table[hashed_val] == 'USED':
        table[hashed_val] = item
    else:
        while table[hashed_val] is not None:
            hashed_val += 1
        table[hashed_val] = item

def search_hash(item, table):
    # Hashes item, checks if it's in the hash table - if it's not where it's expected
    # to be, walks the table until a None is found. Returns a boolean.
    hashed_val = item**2 % len(table)
    if table[hashed_val] == item:
        return True
    elif table[hashed_val] == None:
        return False
    else:
        if table[hashed_val] != item:
            hashed_val += 1
            while table[hashed_val] is not None:
                if table[hashed_val] == item:
                    return True
                hashed_val += 1
        return False

def remove_item(item, table):
    # Searches for an item in the hash table, if it's not in the proper slot,
    # checks until you hit the first None. When the item is found, it's replaced
    # with a marker and returns a boolean.
    hashed_val = item**2 % len(table)
    if table[hashed_val] == item:
        table[hashed_val] = 'USED'
        return True
    elif table[hashed_val] == None:
        return False
    else:
         if table[hashed_val] != item:
            hashed_val += 1
            while table[hashed_val] is not None:
                if table[hashed_val] == item:
                    table[hashed_val] = 'USED'
                    return True
                hashed_val += 1
         return False
