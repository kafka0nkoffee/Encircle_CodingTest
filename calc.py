#!/usr/bin/python

# an S-expression calculator

import sys
from functools import reduce


# to check if the character is an operator or not

def isOperator(value):
    if (value == '+' or value == '*'):
        return True
    else:
        return False


# evaluating the expression

def evaluate(expression):

    # replacing 'add' and 'multiply' with their respective operators
    # for ease of operation

    expression = expression.replace('add', '+').replace('multiply', '*')

    # adding some spaces to handle lack of space
    # around certain opening and closing braces

    expression = expression.replace('(', '( ').replace(')', ' )')

    # store the string expression in a list for ease
    # of dealing with multi-digit values e.g. (add 123 456)

    stringList = expression.split()
    stack = []
    result = 0

    # Traverse through every character of input expression
    for val in stringList:
        if val == ')':
            # start popping elements as needed
            # on encountering a ')'
            operands = []
            while stack:
                temp = stack.pop()
                if temp == '(':
                    stack.append(result)
                    break
                elif not isOperator(temp):
                    # if operand, push into another stack
                    # for later calculation
                    operands.append(int(temp))
                else:
                    # if operator, use the popped operands
                    # to calculate intermediate result
                    if temp == '+':
                        result = reduce((lambda x, y: x + y), operands)
                    if temp == '*':
                        result = reduce((lambda x, y: x * y), operands)
        else:
            # push elements into stack until you encounter a ')'
            stack.append(val)

    # Only element left on the stack will be the final result
    # Exception: if entered string is
    # something like "123 456 789" then there is
    # no evaluation to be done

    if len(stack) > 1:
        return "No evaluation to be done"
    else:
        t = stack.pop()
        return t


# to run from command line in REPL mode

if __name__ == '__main__':
    finalResult = evaluate(sys.argv[1])
    print(finalResult)
