# Regular expresssion used for string manipulation 

import re

my_str = '''this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved watching them horse around forgive the pun well i hope that it has been highly enjoyable typing this paragraph and i wish you the best of luck getting the best score that you possibly can'''


# 1. Find the all occurances of concerned string in given string.
print('\nCase1:')
patt = re.compile(r'this')          
matches = patt.finditer(my_str)
for match in matches:
    print(match)                    
    # match will be of re.Match
    # At output, span will provide the exact location of required data
print(my_str[148:152])

# 2. Find the occurances where concerned data is present after any data. '.' means any.
print('\nCase2:')
patt = re.compile(r'.graph')          
matches = patt.finditer(my_str)
for match in matches:
    print(match)      
print(my_str[20:26])

# 3. It checks whether the given string is starts with concerned string or not
print('\nCase3:')
patt = re.compile(r'^this')          
matches = patt.finditer(my_str)
for match in matches:
    print(match)      

# 4. It checks whether the given string is ends with concerned string or not
print('\nCase4:')
patt = re.compile(r'can$')          
matches = patt.finditer(my_str)
for match in matches:
    print(match) 

# 5. Find the occurances where given leters should be present in given string
print('\nCase5:')
patt = re.compile(r'pi*')           
# '*' means zero or any numbers of occurance of left letter                
matches = patt.finditer(my_str)
for match in matches:
    print(match)

print('\n')
patt = re.compile(r'pi+')           
# '+' means atleast one occurance of left letter                
matches = patt.finditer(my_str)
for match in matches:
    print(match)

# 6. Either or
print('\nCase6:')
patt = re.compile(r'this|capital') # It will search for either 'this' or 'capital'                
matches = patt.finditer(my_str)
for match in matches:
    print(match)



# 7. find sub strings which starts or ends with concerned strings
print('\nCase7\nstarts with:')
patt = re.compile(r'\bpara') 
matches = patt.finditer(my_str)
for match in matches:
    print(match)

print('\nends with:')
patt = re.compile(r'graph\b') 
matches = patt.finditer(my_str)
for match in matches:
    print(match)