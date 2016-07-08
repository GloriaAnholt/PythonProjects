from HashTableOAClass import OAHashTable

ht = OAHashTable()

for i in range(0,100):
    ht.insert(i, i + 10)
   
   
ht.keys() 
ht.values()
ht.items()

print ht.size
print ht.occupancy
print len(ht)


for i in ht.keys():
    print i,

print "/n"

for i in ht.values():
    print i,

print "/n"

for i in ht.items():
    print i,