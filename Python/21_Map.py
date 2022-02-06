# Map function is used to apply given function on each element of a given iterable.

l = [i for i in range(11)]

def sqr(n):
    return n**2

# Method 1
print("Method 1")
result1 = map(sqr,l)
print(list(result1))


# Method 2
print("Method 2")
result1 = map(lambda n: n**2,l)     #Using Lambda function
print(list(result1))

