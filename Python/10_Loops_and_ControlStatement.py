# for loop
# Method 1
print("For loop Method 1")
for i in range(5):
    print(i)

print("\n")
for i in range(0,10,2):         #(start,end,step)
    print(i)

# Method 2
print("\nFor loop Method 2")

l = [1,2,3,4,5]
for i in l:
    print(i)

# While loop
print("\nwhile loop")
i = 0
while i<5:
    print(i)
    i = i+1

# Break 
print("\nBreak ")
i=0
while(1):
    print(i)
    i = i+1
    if i==3:
        break       # It break the execution of the loop 

# Continue
print("\nContinue ")

for i in range(6):
    if i>=3 and i<=4:
        continue    #It stops the Further execution for that iteration and continue with next iteration
    print(i)