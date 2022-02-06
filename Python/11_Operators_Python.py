# Operators are used to perform operations on variables and values.

# 1. Arithmatic Operators
print("\nArithmatic Operators\n")
# Addition
print(5+2)

# Subtraction
print(5-2)

# Multiplication
print(5*2)

# Division
print(5/2)

# Modulus 
print(5%2)      # Gives the remainder 

# Exponentiation
print(5**2)     # To find power

# Floor division        
print(5//2)     # Quotient till decimal point

# 2. Comparison Operators
print("\nComparison Operators\n")

# Equal
print(5 == 5)

# Not Equal
print(5 != 5)

# Greater than
print(5 > 6)

# Less than
print(5 < 10)

# Grater than or Equal
print(4 >= 5)

# Less than or Equal
print(5 <= 6)

# 3. Logical operators
print("\nLogical Operators\n")

x = 5
y =10

# and
print(x>2 and y==10)
print(x<2 and y==10)        # Returns True only when all conditions are True

# or
print(x>2 or y==10)
print(x<2 or y==10)         # Returns True when atleast one condition is True

# not
print(not(x>2 or y==10))
print(not(x<2 and y==10))       # Reverse the result measn True to flase and vise versa


# Membership Operators
print("\nMembership Operators\n")
l = [1,2,3,4,5]

# in
print(5 in l)

# not in 
print(5 not in l)

# Bitwise Operators
print("\nBitwise Operators\n")

# AND
print(5 & 4)   # Performs bitwise AND operation given values 

# OR
print(5 | 4)   # Performs bitwise OR operation given values 
