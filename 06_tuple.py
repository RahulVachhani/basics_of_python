# Tuple   --> Tuple is immutable so we can not change after create once


t1 = (10,203,333)
print(t1)


# t1[2] = 1000  # This is invalid in tuple
print(t1.__dir__())
