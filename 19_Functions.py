
# Functions

# When we use same code in defferent places then we use functions

def func1():            # function is defined using def keyword
    print("Hello")

func1()





# Function with arguments

def add(n1,n2):
    return n1 + n2

print(add(10,33))





# Arguments types

# 1) Positional Argument
# 2) keyword Argument
# 3) Default Argument
# 4) Variable-Length Arguments



# 1) Positional Argument

# In this the argument's position is fixed

def sub(n1, n2):
    return n1 - n2

print(sub(20,10))       # in here 20 is store in n1 and 10 is store in n2




# 2) keyword Argument

# in this we gives the values with it name of parameter

def sub(n1, n2): 
    return n1 -n2

print(sub(n2 = 10, n1 = 20)) 




# 3) Default Argument

# in this we provide the default value tio the perameters

def add(n1=0, n2=0):
    return n1 + n2
print(add())    # here use default value 0 + 0 
print(add(10))  # here 10 is store in n1 and n2 is used default value 10 + 0
print(add(10,40))





# 4) Variable-Length Arguments

# <-- *args -->
# in this funtion takes any number of variable number of positional arguments, store in tuple

def add(*n):            # we can give any number of arguments
    sum = 0
    for i in n:
        sum += i
    return sum

print(add())
print(add(110))
print(add(110,220,330))   


# <-- **kwargs -->
# in this funtion takes any number of variable number of keyword arguments, store in dictionary


def student(**n):
    for i,j in n.items():
        print(f'{i} : {j}')

student(name = "rahul", age = 22, id = 234)

    


