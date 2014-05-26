#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket

MUL = ('mul', 'multiply', '*')
ADD_STRING = ('string', 'merge', '#')
ADD_INT = ('add', '+')
QUIT = ('quit', 'q', 'exit', 'stop')


def standard_package(number):
    package = bytearray()
    package.append(number)


def input_operation():
    global ADD_INT
    global MUL
    global ADD_STRING
    global package_operation

    while(True):
        operation = eval(input('Which operation? (*/+/#/q)'))
        package_operation = bytearray()
        if operation in ADD_INT:
            package_operation.append('+')
            break
        elif operation in MUL:
            package_operation.append('*')
            break
        elif operation in ADD_STRING:
            package_operation.append('#')
            break
        elif operation in QUIT:
            return 0
        else:
            print('Invalid input, try again!')

    return package_operation


def main(argv):
    IP = eval(input('Enter the server IP: '))
    PORT = eval(input('Enter the connection port: '))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while(True):
        package_opc = input_operation()
        if package_opc == 0:
            break
        package_1st = standard_package(int(eval(input('1st operand: '))))
        package_2nd = standard_package(int(eval(input('2nd operand: '))))
        s.send(package_opc)
        s.send(package_1st)
        s.send(package_2nd)
        solution = s.recv()
        print(('The solution is: %i', solution))
    s.close()

if __name__ == "__main__":
    main()