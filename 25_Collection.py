
# Collection

import collections 

# Counter()
a = 'aaabbbsssssssaacc'
count = collections.Counter(a)
print(count)

# Its return most used element
print(count.most_common(1))   # here we give 1 so most common only 1 element is show
print(count.most_common(2))   # here we give 2 so most common only 2 element are show

# print(count.most_common(1)[0][0]) # its show that element only not count

# Its return the individual elements 
print(list(count.elements())) 
 


# namedtuple()
Point = collections.namedtuple('Point', 'x,y')
pt = Point(3,4)
print(pt)
print(pt.x, pt.y)



# OrderdDict()
d = collections.OrderedDict()
d['a'] = 1
d['b'] = 3
d['d'] = 5
d['c'] = 4
print(d)
print(d['a']) 



# DefaultDict()
d = collections.defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['c'])



# Deque()
d = collections.deque()  
d.append(1)
d.append(2)
d.appendleft(3)
d.extend([4,5,6])
d.extendleft([7,8])
print(d)




import collections 


# Counter() - counts the frequency of elements in an iterable (e.g., string)
a = 'aaabbbsssssssaacc'
count = collections.Counter(a)
print("Counter:", count)  



# Get the most common elements (1 most common, 2 most common, etc.)
print("Most common (1):", count.most_common(1))  # Most common element
print("Most common (2):", count.most_common(2))  # Top 2 most common elements

print("Most common element:", count.most_common(1)[0][0])  



# Return the individual elements expanded based on frequency
print("Elements expanded:", list(count.elements())) 




# namedtuple() - creates a lightweight object for grouping data
Point = collections.namedtuple('Point', 'x y')
pt = Point(3, 4)
print("\nNamedtuple Point:", pt)
print("x:", pt.x, "y:", pt.y)




# OrderedDict() - maintains the order of insertion for dictionary keys
d = collections.OrderedDict()
d['a'] = 1
d['b'] = 3
d['d'] = 5
d['c'] = 4
print("\nOrderedDict:", d)  # Ordered by insertion
print("Value of 'a':", d['a']) 




# defaultdict() - returns a default value if a key is missing (int in this case)
d = collections.defaultdict(float)
d['a'] = 1
d['b'] = 2
print("\nDefaultDict:", d)
print("Value of 'a':", d['a'])  # 1
print("Value of 'c' (default int):", d['c'])  # Returns 0 (default for int)




# deque() - a double-ended queue, supports fast appends and pops from both ends
d = collections.deque()
d.append(1)         # Add 1 to the right end
d.append(2)         # Add 2 to the right end
d.appendleft(3)     # Add 3 to the left end
d.extend([4, 5, 6]) # Extend the deque by adding [4, 5, 6] to the right end
d.extendleft([7, 8])# Extend by adding [7, 8] to the left end
print("\nDeque:", d) 
