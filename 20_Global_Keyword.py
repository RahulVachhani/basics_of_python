

# Global Keyword   --> its used for access the variable which is outside the function , inside the function we can use that variable

a = 10

def fun():
    global a
    print(f'Inside the function {a}')

fun()

print(f'Outside the function {a}')





# Another 

b = 200
print(id(b))

def fun1():
    
    x = globals()['b']    # globals is gives all the global var after that we provide name of that var which we want to access
    
    print(id(x))
    print(x)

fun1()
