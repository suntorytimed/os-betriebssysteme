#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket

MUL = ('mul', 'multiply', '*')
SUB = ('sub', 'subtract', '-')
DIV = ('div', 'divide', '/')
ADD = ('add', '+')


def standard_package(number):
    package = bytearray()
    package.append(number)


def input_operation():
    global ADD
    global SUB
    global MUL
    global DIV
    global package_operation

    while(True):
        operation = eval(input('Which operation?'))
        package_operation = bytearray()
        if operation in ADD:
            package_operation.append('+')
            break
        elif operation in SUB:
            package_operation.append('-')
            break
        elif operation in MUL:
            package_operation.append('*')
            break
        elif operation in DIV:
            package_operation.append('/')
            break
        else:
            print('Invalid input, try again!')

    return package_operation


def main(argv):
    IP = eval(input('Enter the server IP: '))
    PORT = eval(input('Enter the connection port: '))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while(True):
        input_operation()
        package_1st = standard_package(int(eval(input('Enter the 1st operand: '))))
        package_2nd = standard_package(int(eval(input('Enter the 2nd operand: '))))

    s.close()

if __name__ == "__main__":
    main()
