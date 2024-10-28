
from functools import reduce

# Anonymous Function 

# lambda function

# When we want use only once then we used lambda function
a = lambda a : a * a       
print(a(10))
print(a(4))


# lambda function with *args (variable types arguments)
b = lambda *x : reduce(lambda x1,x2 : x1 + x2, x)  # its return sum 
print(b(10,20,30))
print(b(20,23))



# Filter  

# when we want some filter based on condition or any function then we use filter
l1 = [1,2,3,4,5,6]
even = list(filter(lambda x : x % 2 == 0, l1))    
print(even)



# map 

# When we want to map any function with sequence then we use map
l2 = [1,2,3,4]
square = list(map(lambda x : x * x , l2))   
print(square)




# reduce -->  from functools import reduce

l3 = [10,20,30,40,50]

total = reduce(lambda a,b : a + b, l3)  # its produce one ans
print(total)