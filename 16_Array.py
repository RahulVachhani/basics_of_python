
# Array is not in built in python we import to use

import array as arr

a = arr.array('i',[1,2,3,4])     # 'i' is indicate type of element which is store in array (Here i indicates 'signed int' type)
print(a)
print(type(a))
print(a[0])



a = arr.array('I',[1,2,3,4])     # 'I' (Here I indicates 'unsigned int' type (means only positive number)
print(a)
print(type(a))
print(a[0])



print(f'The Buffer info : {a.buffer_info()}')    # its saw the address of an array with count elements (here 4)
print(f'The type code is {a.typecode}')     # its saw the type of elements store in array


# a.reverse()     # its reverse the array
# for i in range(len(a)):
#     print(a[i])



# For copy an array to another array
a = arr.array('i',[1,2,3,4]) 
new_arr = arr.array(a.typecode, [i for i in a])
print(new_arr)
print(new_arr[3])




# For empty array 
a = arr.array('i')  # This create empty array
print(a)
num = int(input("How many number you want to add in array!! : "))
for i in range(num):
    value = int(input(f'Enter number {i+1} : '))
    a.append(value)
print(a)


print(a.index(10))  # its return index of given element
