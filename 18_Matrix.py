
# Matrix or Multidimetional array

import numpy as np

# a = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(f'The type is : {a.dtype}') 
# print(f'The dimention is : {a.ndim}')    # its saw the Dimention of an array
# print(f'The rows and column are : {a.shape}')   # its saw the row, colomn like (2,3)


# a = np.array([
#     [1,2,3,6,7,8],
#     [4,5,6,9,10,11]
# ])

# print(f'The conver in any dimention : {a.reshape(3,4)}')    # Its like 3 row and 4 column
# print(f'The conver in any dimention : {a.reshape(2,2,3)}')



# Matrix

m = np.matrix('''1 2 3; 
                 4 5 6;
                 7 8 9''')
print(m)

print(f'The diagonal values : {np.diagonal(m)}')  # return diagonal values 

print(f'The minimum value from matrix : {np.min(m)}')  # return minimum value from matrix

print(f'The maximum value from matrix : {np.max(m)}')  # return maximum value from matrix



# In matrix automatically addition and multiplication are perform 

m1 = np.matrix('''1 2 3;
                  4 5 6;
                  7 8 9 ''')

m2 = np.matrix('''10 20 30;
                  40 50 60;
                  70 80 90 ''')

m3 = m1 + m2
print(m3)


m3 = m1 * m2
print(m3)