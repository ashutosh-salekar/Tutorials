#  reduce() is ued when we need to apply a function to an iterable and reduce it to a single cumulative value. 

from functools import reduce

l = [i for i in range(11)]

# Method 1
print("Method 1")
def sum(a,b):
    return(a+b)

result1 = reduce(sum,l)
print(result1)

# Method 2
print("Method 2")
result1 = reduce(lambda a,b:a+b,l)      # using Lambda function
print(result1)
