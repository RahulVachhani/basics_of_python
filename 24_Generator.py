
# Generator

def gen():
    for i in range(10):
        yield i

g = gen()
print(next(g))
print(next(g))







# iter
a = [10,20,30]
b = iter(a)
print(next(b))
print(next(b))