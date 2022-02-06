# filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.
# Iterable = Iterable is an object, which one can iterate over, like list, tuple, string

l = [i for i in range(11)]

# Method 1
print("Method1")
def even_fun(n):
    return n%2==0

result1 = filter(even_fun,l)
print(list(result1))

# Method 2
print("Method2")
result2 = filter(lambda a: a%2==0,l)      #Using Lambda function
print(list(result2))