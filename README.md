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