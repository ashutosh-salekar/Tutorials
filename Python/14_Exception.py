# Exceptions are the errors occured while executing the program

a = input("Number 1: ")
b = input("Number 2: ")

try:
    divide = int(a) / int(b)
    print("Division: ",divide)      # If values of b is Zero then we can't divide by Zero, Hence  exception will occure.
except Exception as e:
    print("Exception occured:",e)


# There are various types of exception present
# 1. Divide by zero
# 2. add string with integer