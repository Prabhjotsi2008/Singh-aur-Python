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