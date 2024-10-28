
# Finally Keyword


# try:
#     l1 = [10,20,30,40]
#     a = int(input("Enter a index : "))
#     print(l1[a])

# except:
#     print("Error occurs !")

# finally:
#     print('This is always executes')


# BOTH ARE SAME FOR WITHOUT FUNCTION BUT THE DIFFERENCE IS IN THE FUNCTION.

# try:
#     l1 = [10,20,30,40]
#     a = int(input("Enter a index : "))
#     print(l1[a])

# except:
#     print("Error occurs !")

# print('This is always executes')




# in this function we use return so when the the return is called then so finally is always executes
def execute():
    try:
        l1 = [10,20,30,40]
        a = int(input("Enter a index : "))
        print(l1[a])
        return 1
    except:
        print("Error occurs !")
        return 0
    
    finally:                             # finnaly is always return either function return or not
        print('This is always executes')

x = execute()
print(x)