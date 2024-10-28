
# Set  --> Set is Mutable


s = set()    # Create Empty Set
s1 = {10,20}

# Set Methods

# add()
s.add(10)      # add() is used to add an element in set.  Its Just like append() in list
s.add("Rahul")
print(s)

# s.add(s1)      # This gives error
# print(s)


# update()  --> it is used to add multiple value in set or another set,list,tuple as individual elements in set like extend() in list
# update() takes only iterable 

s.update([10,20,30])
print(s)

s.update("Rahul",[100])     # This is Sequence so all elements of all sequence is add as individual in set 
print(s)

s.update(s1)
print(s)


# pop()    --> remove random element in set and return that element
s = {10,20,30}
a = s.pop()
print(s, a)


# Remove()   --> Remove perticuler Element in set
s = {10,20,30}
s.remove(20)       # It does not return any thing
#s.remove(1000)     # Its gives error because 1000 in not in set
print(s)


# discard()   --> remove perticuler element and its does not give any error when element is not present
s = {10,20,30}
s.discard(10)
s.discard(1000)    # Its does not gives error
print(s)





## set operations 

# union()  ==  |  

x = {1,2,3}
y = {2,3,4,5}

z = x.union(y)          # Its combine the all elements of both set , but its does not change in both sets but return another set
print(z) 

print(x)
print(y)


# Intersection()   ==   &
x = {1,2,3}
y = {2,3,4,5}

z = x.intersection(y)
print(z)



# symmetric_difference()   ==  -    

x = {1,2,3}
y = {2,3,4,5}
z = x.symmetric_difference(y)      # Its return all distincts element in both set
print(z)









