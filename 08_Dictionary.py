
# Dictionary

d1 = {1:"rahul", 2:"shyam", "reena":"patel"}
print(d1)
print(d1[1])

d1[3] = "karina"       # Add the item with key = 3 and value = karina
print(d1)



# Dictionary Methods
print(d1.keys())             # keys() return all the keys from dict

print(d1.values())           # values() return all the values from dict

print(d1.items())            # items() return all the key value pair in form of tuple


d2 = {2:"smit", "jinal":30}
d1.update(d2)             # add and update the one dict to another dict
print(d1)                 


print(d1.get(2))   

print(d1.pop('reena'))       # pop() remove the element with any key and return that key's value

print(d1.popitem())      

print(d1)

# print(d1.pop())  <-- This will give an error