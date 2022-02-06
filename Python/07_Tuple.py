# Tuples are used to store multiple items in a single variable. Tuples are immutable means we can't modify them.

tup = (1,2,3,4,5,6,7)
print(tup,"\nType:",type(tup))

# To access perticular element of tuple
print(tup[2])
print(tup[0:6:2])

# Add two tuples
tup1 = (1,2,3)
tup2 = (5,6,7)
tup3 = tup1 + tup2
print(tup3)
