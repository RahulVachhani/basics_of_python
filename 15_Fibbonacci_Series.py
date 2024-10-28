
# Write a program to get a fibonacci series


n = int(input("Enter the number : "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

for i in range(n):
    print(a)
    a,b = b,a+b


print()
print("With function :")

# With Function

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n == 2:
        print(a+b)
    else:
        for i in range(2,n):
            print(a)
            a,b = b, a+b

fib(15)