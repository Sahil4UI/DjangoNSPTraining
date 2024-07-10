Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Tuple - Python's immutable and ordered data collection
x = (1,2,3,4)
type(x)
<class 'tuple'>
x[0] = -1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x[0] = -1
TypeError: 'tuple' object does not support item assignment

x = (i for i in range(1,11))
x#generator->obj
<generator object <genexpr> at 0x103277e80>
print(x)
<generator object <genexpr> at 0x103277e80>
for i in x:
    print(i)

1
2
3
4
5
6
7
8
9
10
x
<generator object <genexpr> at 0x103277e80>
list(x)
[]
x
<generator object <genexpr> at 0x103277e80>
x[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x[0]
TypeError: 'generator' object is not subscriptable
help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.
 |
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

x = (1,2,3,4,5)
min(x)
1
max(x)
5
sum(x)
15
roll = [1,2,3,4,5]
name = ["]
        
SyntaxError: unterminated string literal (detected at line 1)
name = ["ravi","sam","rahul","dev","ankit"]
        
roll
        
[1, 2, 3, 4, 5]
name
        
['ravi', 'sam', 'rahul', 'dev', 'ankit']
list[zip(roll,name)]
        
list[<zip object at 0x1035b6780>]
zip(roll,name)
        
<zip object at 0x102e344c0>
x = zip(roll,name)
        
x
        
<zip object at 0x102e22b00>
for i in x:
        print(i)

(1, 'ravi')
(2, 'sam')
(3, 'rahul')
(4, 'dev')
(5, 'ankit')
marks = []
        
zip(roll,name,marks)
        
<zip object at 0x103330d40>
x = zip(roll,name,marks)
        
for i in x:
        print(i)

for i in x:
    print(i)

marks = [1,2]
        
for i in zip(roll,name,marks):
    print(i)

(1, 'ravi', 1)
(2, 'sam', 2)


x
        
<zip object at 0x1035bebc0>
name
        
['ravi', 'sam', 'rahul', 'dev', 'ankit']
marks = [100,90]
        
#dictionary
        
x = {}
        
type(x)
        
<class 'dict'>
x = {1,2,3}
        
type(x)
        
<class 'set'>
x = {"roll":1}
        
x
        
{'roll': 1}
x["name"]="Sahil"
        
x
        
{'roll': 1, 'name': 'Sahil'}
x["name"]="Ram"
        
x
        
{'roll': 1, 'name': 'Ram'}
x["contact"] = 9876543210
        
x
        
{'roll': 1, 'name': 'Ram', 'contact': 9876543210}
x.pop("contact")
        
9876543210
x
        
{'roll': 1, 'name': 'Ram'}
x.get("roll")
        
1
x["roll"]
        
1
x.keys()
        
dict_keys(['roll', 'name'])
x.values()
        
dict_values([1, 'Ram'])
x.items()
        
dict_items([('roll', 1), ('name', 'Ram')])
x
        
{'roll': 1, 'name': 'Ram'}
x.popitem()
        
('name', 'Ram')
x
        
{'roll': 1}
x ={'roll': 1, 'name': 'Ram', 'contact': 9876543210}
        
len(x)
        
3
