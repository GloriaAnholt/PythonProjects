


d = {"a": 1, "b":2, "c":3}

# Entire dictionary
print d

# Print just the keys, in whatever order they exist in
for key in d:
	print key
	
# Print just the values
print d.values()

# Print both keys and values as a list of tuples
print d.items()

# Print the key, then the value, from the tuple of items
for key, val in d.items():
	print key, val
