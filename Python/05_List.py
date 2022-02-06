# Lists are used to store multiple items in a single variable. we can store data with different types.

l = ["apple","Mango","grapes","banana","orange","kiwi"]
print(l,"\nType:",type(l))

# Access elements of the list separately.
print(l[0])
print(l[1]) 
print(l[0:5:2])

# Insert element in the list at perticular location
l.insert(2,"pineapple")   # Insert "pineapple" at 3rd location
print(l)

# append list/ insert element at the last
l.append("papaya")
print(l)  

# Get index of perticular data from list
print(l.index("papaya"))

# Delete data from perticular location
l.remove("papaya")  # With actual data value
print(l)

l.pop(2)            # With index of element
print(l)

# Add two list
l1 = [1,2,3]
l2 = [5,6,7]
l3 = l1 + l2
print(l3)

# Max and Min of list
print("Max:",max(l3))
print("Min:",min(l3))