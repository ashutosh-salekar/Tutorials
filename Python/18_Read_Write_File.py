# f = open(path,mode)  It will open the file whose pathe is given in the given mode.
# modes:
    # 'r' : we can only read the file
    # 'w' : we can only write the file
    # 'a' : we can only append the file
    
# NOTE : Try to use 'with' method to open a file as it closes the file automatically at the end.
# cheat-sheet : https://docs.python.org/3/library/functions.html#open

print('----- Witing file -----\n')
# Creatig a new file
f = open("ReadWriteFile.txt","w")
f.write("Join hands to save environment.")
f.close()

# Append the data in aleady created file
f = open("ReadWriteFile.txt","a")
f.write("\nOnly One Earth.")
f.close()

print('----- Reading file -----\n')
# Reading file
# read(): Will read all remaining containt in the file from current position
# readline(): Will read only one line from the file from current position
# readlines(): Will return  list containing all lines from the file

# Method 1
print('----- Method 1 -----\n')
with open("ReadWriteFile.txt","r") as f:
    print(f.readlines())


# Method 2
print('----- Method 2 -----\n')
f = open("ReadWriteFile.txt","r")
print("Reading method 1")
print(f.read())

# Method 3
print('----- Method 3 -----\n')
print("Reading method 2")
f = open("ReadWriteFile.txt","r")
for line in f:
    print(line.rstrip())        # rstrip() will remove the "\n" at the end of each line


