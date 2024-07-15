#user defined functions
'''
def f1(x,y):
    print(x+y)
'''
'''
def f1(x,y):
    return x+y
'''
'''
f1 = lambda x,y : x+y
'''
'''
f1 = lambda x : "Even" if (x%2==0) else "Odd"
print(f1(12))
'''
'''
def f1():
    def f2():
        print("f2 called")
    def f3():
        print("f3 called")
    return f2,f3

print(f1())
'''
'''
import functools as ft
x = [i for i in range(1,11)]
def f1(x,y):
    return x+y

res=ft.reduce(f1,x)
print(res)
'''
'''
x = [i for i in range(1,11)]
square = lambda a:a**2
print(list(map(square,x)))
'''
'''
def f1():
    for i in range(1,11):
        yield i
print(f1())
'''
x = [i for i in range(1,11)]
f1 = lambda x : True if (x%2==0) else False
print(list(filter(f1,x)))
print(filter(f1,x))

