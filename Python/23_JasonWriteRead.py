import json

# Writing a Json file
"""
Jdic = {}
Jdic['stud1'] = {"Name":"Ashu","Age": 21, "Gender":"Male"}
Jdic['stud2'] = {"Name":"Tony","Age": 22, "Gender":"Male"}
Jdic['stud3'] = {"Name":"Jack","Age": 22, "Gender":"Male"}

s = json.dumps(Jdic)        #convert the dictionary into json string
# print(s)

with open("JsonWriteRead.txt","w") as f:
    f.write(s)
"""

# Reading a Json file
f = open("JsonWriteRead.txt","r")
p = f.read()   # We will get Whole Json file as a single string

data = json.loads(p)  # Here we get dictionary from string
for i in data:
    print(data[i])

for i in data:
    print(data[i]['Name'])
