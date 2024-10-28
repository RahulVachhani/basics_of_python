

# Exception Handling 

b = 5  

try:
    print("In the try block")
    
    
    a = int(input("Enter a number: "))  
    c = a / b
    print(f"Result of division: {c}")


# Handle division by zero error
except ZeroDivisionError as e:
    print("Error: You cannot divide any number by 0.")


# Handle invalid input error (like when input is not an integer)
except ValueError as e:
    print("Error: Invalid input, please enter a valid integer.")

# The finally block always executes
finally:
    print("Inside the finally block")



# Important --> we can only write 'except' instead of 'except Exception as e'