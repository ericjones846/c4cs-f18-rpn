#!/usr/bin/env python3

import operator
import readline
from termcolor import colored
import click

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg, debug):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        if debug:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

@click.command()
@click.option('--debug', is_flag=True, help="Print more output.")
def main(debug):
    while True:
        result = calculate(input("rpn calc> "), debug)
        if result < 0:
            print("Result: ", colored(result, 'red'))
        else:
            print("Result: ", result)

if __name__ == '__main__':
    main()
