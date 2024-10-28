
# Regular Expression

import re

# This mean first latter is Capital and after that omputer
pattern = r"[A-Z]omputer"

text = '''A computer is a machine that can be programmed to automatically carry out sequences 
of arithmetic or logical operations (computation). Modern digital electronic Computers can perform 
generic sets of operations known as programs. These programs enable computers to perform a wide range 
of tasks. The term computer system may refer to a nominally complete computer that includes the hardware,
 operating system, software, and peripheral equipment needed and used for full operation; or to a group 
 of computers that are linked and function together, such as a Computer network or computer cluster.
'''

# # re.search() is return first occurance only
match = re.search(pattern,text)
print(match)


# re.findall() is return all the occurance 
matches = re.findall(pattern, text)
print(matches)


# re.finditer() is find the all the occurance but give one at a time like iterator
matches = re.finditer(pattern,text)
for match in matches:
    print(match)

text = "This is lion"

# re.sub() is replaced the the text with new one and return the new text
new_text = re.sub('lion','elephant',text)
print(new_text)


