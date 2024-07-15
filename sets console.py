Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
name = ["ram","sam","ravi"]
id = [101,102,103]
data = [(k,v) for i in zip(id,name)]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data = [(k,v) for i in zip(id,name)]
NameError: name 'k' is not defined
data = [(k,v) for (k,v) in zip(id,name)]
data
[(101, 'ram'), (102, 'sam'), (103, 'ravi')]
data = {k,v for k,v in zip(id,name)}
SyntaxError: did you forget parentheses around the comprehension target?
data = {(k,v) for k,v in zip(id,name)}
data
{(101, 'ram'), (102, 'sam'), (103, 'ravi')}
x ={"id":101,"name":"ravi"}
x.clear()

========= RESTART: /Users/sahilkumar/Desktop/TPDDL1/dictionary1.py ========
101 rahul A+
102 rahul B
103 ram A
data = {k:v for k:v in zip(id,name)}
SyntaxError: invalid syntax
data = {k:v for (k,v) in zip(id,name)}
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    data = {k:v for (k,v) in zip(id,name)}
NameError: name 'name' is not defined
id = [101,102,103]
name = ["ram","sam","ravi"]
data = {k:v for (k,v) in zip(id,name)}
data
{101: 'ram', 102: 'sam', 103: 'ravi'}
data.items()
dict_items([(101, 'ram'), (102, 'sam'), (103, 'ravi')])

========= RESTART: /Users/sahilkumar/Desktop/TPDDL1/dictionary1.py ========
101 rahul A+
102 rahul B
103 ram A
    id   name grade
0  101  rahul    A+
1  102  rahul     B
2  103    ram     A
x = {1,1,1,2,2,2,3,3,3,3}
x
{1, 2, 3}
#set->no indexing , duplicates not allowed
x
{1, 2, 3}
for i in x:
    print(i)

1
2
3
x.add(22)
x
{1, 2, 3, 22}
x.discard(22)
x.discard(0)
x
{1, 2, 3}
x.add(1.0)
x.add(True)
x
{1, 2, 3}
x
{1, 2, 3}
x = "a"
x
'a'
x = {1, 2, 3, 22}
x.add("a")
x
{1, 2, 3, 'a', 22}
x.add("b")
x
{1, 2, 3, 'b', 'a', 22}
x.add("hello")
x
{1, 2, 3, 'b', 'a', 'hello', 22}
x.clear()
x
set()
#union
x = {1,2,3,4,5}
y = {4,5,6,7}
x.union(y)
{1, 2, 3, 4, 5, 6, 7}
x+Y
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x+Y
NameError: name 'Y' is not defined. Did you mean: 'y'?
x+y
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x+y
TypeError: unsupported operand type(s) for +: 'set' and 'set'
x
{1, 2, 3, 4, 5}
y
{4, 5, 6, 7}
>>> x.update(y)
>>> x
{1, 2, 3, 4, 5, 6, 7}
>>> x = {1, 2, 3, 4, 5}
>>> x
{1, 2, 3, 4, 5}
>>> y
{4, 5, 6, 7}
>>> x-y
{1, 2, 3}
>>> x.difference(y)
{1, 2, 3}
>>> x.difference_update(y)
>>> x
{1, 2, 3}
>>> x = {1, 2, 3, 4, 5}
>>> x.intersection(y)
{4, 5}
>>> x.intersection_update(y)
>>> x
{4, 5}
