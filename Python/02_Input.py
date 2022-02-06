# We use "input" keyword to take input from user while executing the code.
name = input("enter the Name: ")
print("Name:",name)

# Taking multiple input
a,b,c = input("enter 3 values with space separation:").split()
print("a:",a," b:",b," c:",c)

# By default "split" uses Space as separator. If we want to use another separator we have to mention that. 
p,q,r = input("enter 3 values with forward slash separation:").split("/")
print("p:",p," q:",q," r:",r)