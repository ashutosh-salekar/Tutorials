# # *args and **kwargs usefule when we dont know the exact count of the arguments should be passed to function.

# *args is tuple type and store all values passed to function
def addition(*args):
    add = 0
    for i in args:
        add += i
    return add

ret1 = addition(1,2,3,4,5)
print(f"Addition of given numbers is {ret1}.")


# **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments. 
# data typw of kwargs will be dict
def combine(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

ret2 = combine(a="Hello", b="world", c="!")
print(f"Combination of all given strings is {ret2}.")