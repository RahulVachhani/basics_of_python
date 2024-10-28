
# Write a program check whether given number is prime or not

# num = int(input("Enter the number : "))

# if num < 2:

#     print(f"The number {num} is not prime number")

# else:

#     for i in range(2,(num//2)+1):
#         if num % i == 0:
#             print(f'The number {num} is not prime number')
#             break
#     else:
#         print(f"The number {num} is prime number")





# Write a program to give all prime number in given range

num1 = int(input("Enter the range : "))

for i in range(2,num1):
    prime = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)






            
            