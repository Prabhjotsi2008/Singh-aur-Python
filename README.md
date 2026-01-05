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