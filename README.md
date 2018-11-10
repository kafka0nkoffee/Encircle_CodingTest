Solution to S-expression calculator
=======================

Problem Statement
-----------------

Write a command line program that acts as a simple calculator: it takes a
single argument as an expression and prints out the integer result of
evaluating it.

Assuming the program is implemented in Python, invocations should look like:

    $ ./calc.py 123
    123

    $ ./calc.py "(add 12 12)"
    24

Solution Explanation
--------------------

- adding some spaces to handle lack of space around certain opening and 
  closing braces e.g. (add 2 (multiple 3 3) 8) into ( add 2 ( multiple 3 3 ) 8 )
  to aid the processing of the expression
- store the string expression in a list for ease of dealing 
  with multi-digit values e.g. (add 123 456)
- use a stack to handle pushing and popping elements and holding operands 
  for running operations on
  
Assumptions
-----------

A list of assumptions that were allowed to make:

- A function call is always delimited by parenthesis ( and ).

- Since numbers are specified by digits only, you don't have to deal with
  inputting negative numbers.

- Depending on your choice of language, you may have to pick a data type to
  represent your integers and calculations. Pick something that gives you at
  least 32 bits. None of the calculations will deal with numbers larger than
  that and you won't be penalized for not dealing with overflow.

- You can be pretty lax about error handling. Throwing an exception when in an
  invalid state is fine.

  The tested examples will always be well formed. That means that:

  - Parenthesis will always be balanced.
  - Only the `add` and `multiply` functions will be called.
  - There will always be a single space between the function arguments.


  
