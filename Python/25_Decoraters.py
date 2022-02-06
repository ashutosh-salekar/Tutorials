"""
Decoraters : 
    A decorator in Python is a function that takes another function as its argument, 
    and returns yet another function.
"""
def decorate(func):
    def add_from_list(lis):
        result = []
        for tup in lis:
            result.append(func(tup[0],tup[1]))
        return result
    return add_from_list


@decorate
def add_two_number(a,b):
    return a+b
# Here we have create a function which return the addition of two numbers.

# We have a different use case in which we have a list of tuples with two element. and we want the addtion of elments of tuple. But we can't pass the list as it is to this function. So we use decoraters to get our work done.     


l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
ret = add_two_number(l)
print(ret)

