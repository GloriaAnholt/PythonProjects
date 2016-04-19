# Algorithms and Data Structures: Binary Search
# 4.19.2016
# @totallygloria

'''
Uses a python list to hold the values in the hash table.
Hash function is a basic module arithmetic:
   h(item) = item % table_size
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


htable = create_table(5)
insert_hash([60,33,17,12,24,21,52,72,66,74,89], htable)
print htable