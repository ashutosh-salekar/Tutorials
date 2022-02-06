# A function is a block of code which only runs when it is called. We can pass data, known as parameters, into a function. A function can return data as a result.

# def FunctionName(Parameters):
#     body
#     return Parameters

def add(a,b):               # Defination of function
    c =a + b
    return c                # A function can return multiple valuesin the form of tuple

p,q = 5,9
result = add(p,q)           # Call the function
print("Summation of two numbers is:",result)