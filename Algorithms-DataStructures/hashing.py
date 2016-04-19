# Algorithms and Data Structures: Binary Search
# 4.19.2016
# @totallygloria

'''
Uses a python list to hold the values in the hash table.
Hash function is a basic module arithmetic:
   h(item) = item % table_size
If there's a collision, converts the slot to a list and appends
the new element to the list.
'''


def create_table(len):
    # Returns a list 2x the desired length, populated with None
    return ([None] * (2 * len))

def insert_hash(items, table):

    size = len(table)
    for item in items:
        hashed_val = item % size
        print "hashed value is", hashed_val
        if table[hashed_val] == None:
            table[hashed_val] = item
            print "inserting", item, "in slot", hashed_val
        else:
            if isinstance(table[hashed_val], list):
                table[hashed_val].append(item)
                print "appending", item, "to slot", hashed_val
            else:
                temp = table[hashed_val]
                table[hashed_val] = []
                table[hashed_val].append(temp)
                table[hashed_val].append(item)
                print "converting slot", hashed_val, "to a list with items", temp, item

def search_hash(item, table):

    hashed_val = item % len(table)
    if isinstance(table[hashed_val], int):
        return table[hashed_val] == item
    else:
        for val in table[hashed_val]:
            if item == val:
                return True
    return False




htable = create_table(5)
insert_hash([60,33,17,12,24,21,52,72,66,74,89], htable)
print "33 in table:", search_hash(33, htable)
print "52 in table:", search_hash(52, htable)
print "11 in table:", search_hash(11, htable)