

# List: It is a mutable datatype, meaning we can change its elements after creating it.


# Creating a List
l1 = [10, 20, 30]  # List created using []
print(l1)         
print(l1[1])       # (Accessing list element by index)



# Lists can store heterogeneous data types like int, string, bool, float, etc.
l2 = [10, "Rahul", True, 22.333]
print(l2)         


# List Methods
l3 = [10, 20, "Rahul"]
print(f'Before change list: {l3}')  



# 1. append() - Adds an element at the end of the list
l3.append(40)
print(f'After append 40 in list: {l3}')  



# 2. insert() - Inserts an element at a specified index
l3.insert(0, "Meet")  # Insert "Meet" at index 0
print(f'After insert "Meet" at index 0: {l3}')  #



# If the index is out of range, the element is added at the end of the list
l3.insert(9, 100)  # Insert 100 at index 9 (which is out of range)
print(f'After insert 100 at out-of-range index: {l3}')  



# 3. extend() - Extends the list by adding elements from another iterable (like another list)
l4 = [10, 20, 30]
l5 = [40, 50]
l4.extend(l5)
print(f'After extend another list: {l4}')  # Output: [10, 20, 30, 40, 50]

# l4.extend(10)  # <-- This gives an error because 10 is not an iterable



# 4. pop() - Removes and returns the last element (or the element at a specific index)
l5 = [10, 20, 30, 40]
pop_element = l5.pop()  # Removes the last element and returns it
print(f'After pop element = {pop_element}, remaining list: {l5}')  



# 5. remove() - Removes the first occurrence of the element from the list
l5.remove(10)
print(f'After removing 10 from list: {l5}')  



# 6. sort() - Sorts the list in ascending order
l6 = [50, 10, 30, 20]
l6.sort()
print(f'Sorted list: {l6}')  
