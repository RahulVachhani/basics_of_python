
# Numpy

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3],[4,5,6]], int)      # In numpy we can create multidimentional array
print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[0][1])

print(arr.dtype)   # its saw the type of arr





# Multiple ways to create Array in numpy

# linespace
a = np.linspace(0,10,10)      # here 0 is start, 10 is stop(including), last 10 is part (not step)
print(a)

# arange
b = np.arange(0,10,2)     # here arange is like range 
print(b)
print(type(b))

# ones
c = np.ones(10,int)       # its create array with only value 1 , here we give 10 so 1 is add 10 times in array
print(c)





# add some values in existing array
a = np.array([10,20,30],int)

a = a + 5  # here we add 5 to all element present in a list
# Intead of 5 , we can give any other array also
print(a)




# Copy an array to another array

a = np.array([1,2,3],int)
print(id(a))

b = a               # Here we use aliasing means both variable refer to same array in memory, if any change made in any array then reflect to another array
print(id(b))

b[0] = 10
print(f'Aliasing = {a},{b}')



# Shallow Copy


a = np.array([1,2,3],int)
# print(id(a))

b = a.view()       # Here Modifying b also changes the original array a, since b is just a view of the same data in memory.
# print(id(b))
b[0] = 10
print(f'Shallow Copy = {a},{b}')



# Deep Copy
a = np.array([1,2,3],int)

b = a.copy()    # Here we use deep copy so we can change any thing then does not affect in another array, both are different

b[0] = 10
print(f'Deep Copy = {a},{b}')
