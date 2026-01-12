# Python BTS 


## WORKFLOW
`Source Code (.py)` --> goes to interpretor (cpython) --> `Byte Code (.pyc)` --> goes to PVM --> `Machine Code` --> ready for execution


## EXPLANATION IN-DEPTH
Python first compiles the source code into bytecode (.pyc).
This bytecode is not machine code; it is Python-specific.
The Python Virtual Machine (PVM) acts as a runtime engine that
executes the bytecode instruction by instruction.


## Python Virtual Machine (PVM)
* Code loop to iterate byte code
* Runtime Engine
* Also known as `Python Interpreter`


## Details
* Byte code is `NOT` machine code
* Byte code is `Python specific interpretation`
* `cpython` is standard implementation
* Others are `jython, IronPython, Stackless, PyPy`
* Bytecode is `platform-independent` but `implementation-dependent`

---

# Python in Shell

* Learnt how we can run python in `terminal`
* `import` is used to import other files/modulus to our code
* We can access values using . notation as follows:
``` python
hello_chai.chai("Ginger Tea") # use chai() function
os.getcwd() # current working directory
sys.platform # it returns the device type like 'win32' etc.
```
* What if we make changes in the original module ? Will the change occur in the imported one ? 
* Let's see :
``` python
hello_chai.chai_one # attribute not found # as it is added lately
```
* NO, we have to use following command to reload the imported code: 
``` python
from importlib import reload
reload(hello_chai) # it reloads the changes made
```
* Now you can access new data:
``` python
hello_chai.chai_one # 'lemon tea'
```

--- 

# Mutable and Immutable in Python
* When we create a variable as:
``` python
username = "Prabh"
```
* A memory is allocated which contains value `"Prabh"`
* While `username` points towards that allocated memory

## Mutable Types
* Value can be changed, means the `actual value allocated in the memory` (not the one pointed to)
* Examples : `list`, `dict`, `set`, `bytearray`, and `most user-defined classes`

## Immutable Types
* The value `allocated in the memory` cannot be changed
* However we can change the value `pointed by the variable`
* Examples : `int`, `float`, `bool`, `string (str)`, `tuple`, `frozenset`, `bytes`

## EXAMPLE CODE :
``` python
x = 10 # memory allocated with value "10" # x points to the allocated memory
y = x # y also points to the same memory address as x

print(x) # 10
print(y) # 10

x = 15 # Now a new memory with value "15" is created and x points to this memory address

print(x) # 15
print(y) # 10 # as y still points to "10"
```

> In Python, variables are references to objects.
Mutable objects can be modified in place, while immutable objects require creation of a new object upon modification.

## Data-types (Object-types)

- Number : `1234`, `3.14`, `3+4j`, `0b111`, `Decimal()`, `Fraction()`

- String : `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`

- List : `[1, 2, 3]`, `['abc', 2, 4.5, [3, 4]]`, `list(range(10))`

- Tuple : `(1, 2, 3)`, `('abc', 2, 4.5, (3, 4))`, `tuple("spam")`

- Dictionary : `{'food': 'Spam', 'quantity': 4, 'color': 'pink'}`, `dict(food='Spam', quantity=4, color='pink')`

- Set : `{'spam', 'eggs'}`, `set(['spam', 'eggs'])`, `set(range(5))`

- Files : `open('data.txt')`, `open(r'c:\path\to\file.txt', 'r')`

- Boolean : `True`, `False`
- NoneType : `None`
- Functions, modules, classes

- Advance : `decorators`, `generators`, `iterators`, `MetaProgramming`

---

# BTS of Iteration

## COMPONENTS
- **Iteration Tool :** The tools used for iterating over a data *e.g.* `for`, `comprehesion (list or dict-comprehension)`, `map`, `while`

- **Iterable Objects :** The data structure on which iteration is done *e.g.* `list`, `dict`, `set`, `file`

- **`__next__`** or **`next()`** : This method returns the next value from the iterator.
If no further values are present, it raises the `StopIteration` exception, signaling the end of iteration.


## WORKFLOW
- `iterable tool` sends a method `iter()` to the `iterable object`, `iter()` has the first memory reference of `iterable object`

- The `iterator object` provides values one by one using `__next__()` or `next()`.

- When all values are exhausted, a `StopIteration` exception is raised, indicating the `end of the iterable object.`

## Example CODE
```
>>> myList = [1,2,3,4]
>>> I = iter(myList) # points to first memory reference
>>> I
<list_iterator object at 0x000001F7A36A0C10>
>>> print(I)
<list_iterator object at 0x000001F7A36A0C10>
>>> I.__next__()
1
>>> I # memory reference remains same
<list_iterator object at 0x000001F7A36A0C10> # signifies that iter() always point to the first memory reference
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__() # throws error as end reached
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
```
> The iterator object remains the same, but its internal position moves forward after each __next__() call.

## FILE-HANDLING

1. `General Method` *using readline()*
```
>>> f = open("chai.py")
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "hitesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
```
- It is able to handle end of file `without raising an exception`
- It gived `'' (empty string)` signifying `end of file`

2. `Raw Method` *using __next__()*
```
>>> f = open("chai.py")
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
```
- Directly uses the iterator protocol
- Since it is a `raw method`, so the termination (end) of file is `not handled nicely`
- It raises `StopIteration` once EOF is reached

3. `LOOP`in file
- `CODE:`
``` python
f = open("chai.py")
# for loop
for line in f:
    print(line, end="")
# while loop
while True:
    line = file.readline()
    if not line: break
    print(line,end="")
# both loop gives same output (just different syntax)
```
> `for` loop internally uses `iter()` and `next()`

- `OUTPUT:`
```
import time
print("chai is here")
username = "hitesh"
print(username)
```

4. `iter()` in `FILE HANDLING`
```
>>> f = open("chai.py")
>>> iter(f) is f # iter(f) is same as f for FILES only 
True # bcoz open() itself does iter() in BTS
>>> iter(f) is f.__iter__()
True
```
- File objects are `self-iterators`

- `open()` already prepares the file object for iteration

- Unlike lists, `iter(f)` returns the same object

## FINAL TAKE
Iteration in Python is driven by protocols, not syntax

- for loops, file reading, generators, and comprehensions all rely on:

    - `__iter__()`

    - `__next__()`

    - `StopIteration`