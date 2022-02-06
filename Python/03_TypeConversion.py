# By default "input" take values in string format. Hence even if we enter the integer value it get converted to string. 

age = input("Enter age: ")
print("age:",age,"\ntype of data:",type(age))

# We have to perform type conversion in such cases.
age1 = int(input("Enter age: "))
print("age:",age1,"\ntype of data:",type(age1))


# Some examples of type conversion

a = "2"+"3"
print(a,type(a))

b = 2+3
print(b)

c = int("2"+"3")
print(c,type(c))
