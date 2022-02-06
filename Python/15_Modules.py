# A module is a file consisting of Python code. A module can define functions, classes and variables.

# Python has number of bulit in modules like math, time, random etc.
# We can create our own module and use them for our convenience.

# We have define 4 functions which performs mathematical operation in the "MathsModule.py" file. To use these function in this file we have to import the "MathsModule.py"
import MathsModule

print(dir(MathsModule))   # we will get the list of function in the "MathsModule.py"

num1 = int(input("number1: "))
num2 = int(input("number2: "))

ret1 = MathsModule.add(num1,num2)
print(ret1)

ret2 = MathsModule.multiply(num1,num2)
print(ret2)
