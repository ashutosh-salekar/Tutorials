# Dictionaries are used to store data values in key:value pairs.

dict1 = {"Ashu":21,"tony":22,"captain":80}
print(dict1,"\nType:",type(dict1))

# Access perticular element of dictionary object. Dictionary don't work with index like list and strings
print(dict1["captain"])

# Delete element from dictionary
dict1.pop("captain")
print(dict1)

# Get list of all key:value pairs in tuple
l = dict1.items()
print(l)

# Get all keys of given dictionary
keys = dict1.keys()
print(list(keys))

# Get all values of given dictionary
values = dict1.values()
print(list(values))