
# Custom Errors

a = int(input('Enter any number between 5 to 9 : '))

if a < 5 or a > 9:     # If user not enter number between 5 to 9 then raise valuerror occurs and not execute further program after that
    raise ValueError("Enter the number between the 5 to 9 ")
 
print(a)




