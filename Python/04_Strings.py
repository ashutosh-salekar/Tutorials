#  String is nothing but the array of characters.

s = "Ashutosh"
print(s,type(s))

# Add two strings
s1 = "Ashu"
s2 = "tosh"
s3 = s1 + s2  
print(s3)

# Multiply string
s4 = "Ashu"
s5 = s4 * 3
print(s5)

# Access perticular chracters from string
s6 = "India is my country"
print(s6[0])   # we have to pass the index of the character of which we have to access.

# We can access a set of characters from given string. We have to pass index in [start:end:step]format. end index is exclusive.
print(s6[0:5])
print(s6[0:15:2])

# separate out each word of given string
s7 = "India is my country"
words = s7.split()
print(words)

# separate out each characte of given string
s7 = "India is my country"
words = list(s7)
print(words)