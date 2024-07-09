Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Loops - repetition
for i in range(1,6):
    print(i)

1
2
3
4
5

for i in range(5,0,-1):
    print(i)

5
4
3
2
1
for i in reversed(range(1,6)):
    print(i)

5
4
3
2
1

for i in range(1.5,10.5,1):
    print(i)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for i in range(1.5,10.5,1):
TypeError: 'float' object cannot be interpreted as an integer
x = 1.5
for i in range(1,10):
    print(x)
    x+=i

1.5
2.5
4.5
7.5
11.5
16.5
22.5
29.5
37.5

>>> for i in range(1,11,2):
...     print(i)
... 
1
3
5
7
9
>>> x =
SyntaxError: invalid syntax
>>> x = 1
>>> ++x
1
>>> x
1
>>> x++
SyntaxError: invalid syntax
>>> x--
SyntaxError: invalid syntax
>>> ++x
1
>>> 
