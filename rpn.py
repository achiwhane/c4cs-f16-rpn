#!/usr/bin/env python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def mult(a, b):
    return a * b

def div(a, b):
    return a / b

op_table = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculate(string):
    parsed_input = string.split()
    stack = []

    for token in parsed_input:
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = op_table[token]
            result = function(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError

    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
