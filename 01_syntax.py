print('hello')



# a = eval(input("Enter you want : "))
# print(type(a), a)

print(chr(65))
print(ord('A'))

# l = [ (i * i)-2 if i % 4 == 0 else i * i for i in range(1,21) if i % 2 == 0 ]
# print(l)


# words = ['apple', 'date', 'banana', 'cherry', 'fig']
# d = {i:len(i) for i in words if len(i)>4}
# print(d)

# def pro(*n):
#     if n:
#         p = 1
#         for i in n:
#             p = p * i
#         return p
#     return None
# print(pro(10,3,5,6,7,8,9))


# a = lambda x,y : (x+y) > 100 
# print(a(100,20))


# with open('02_Data_Types.py','r') as f:
#     print(f.read())
    

# def fun1():
#     x = 88
#     def fun2():
#         print(x)
#     return fun2

# print(fun1()())



# def f():
#     print(x)

# x = 10
# f()



# def fun1(num):
#     def fun2(x):
#         print(x ** num)
#     return fun2
# f = fun1(2)
# f(3)

# print(fun1(2)(3))

# # For finding the sub string
# for i in range(len(string)):
#     for j in range(i+1,len(string)+1):
#         s = string[i:j]





# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# aabbbccde

s = input()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
sorted_characters = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    
# Get the top three characters
for i in range(3):
    char, count = sorted_characters[i]
    print(f"{char} {count}")
    