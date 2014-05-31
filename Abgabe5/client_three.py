#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket
import struct

MUL = ('mul', 'multiply', '*')
ADD_STRING = ('string', 'merge', '#')
ADD_INT = ('add', '+')
QUIT = ('quit', 'q', 'exit', 'stop')


def input_operation():
    global ADD_INT
    global MUL
    global ADD_STRING
    global package_operation

    while(True):
        operation = input('Which operation? (*/+/#/q) ')
        package_operation = bytearray()
        if operation in ADD_INT:
            package_operation.append(0)
            break
        elif operation in MUL:
            package_operation.append(1)
            break
        elif operation in ADD_STRING:
            package_operation.append(2)
            return 1
        elif operation in QUIT:
            return 0
        else:
            print('Invalid input, try again!')

    return package_operation


def main():
    IP = input('Enter the server IP: ')
    PORT = eval(input('Enter the connection port: '))
    BUFFER_SIZE = 1400

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while(True):
        package_opc = input_operation()
        if package_opc == 0:
            break
        elif package_opc == 1:
            package_1st = input('1st operand: ')
            package_2nd = input('1st operand: ')
            s.send(package_opc)
            s.sendall(package_1st)
            s.sendall(package_2nd)
        else:
            package_1st = struct.pack('!i', int(input('1st operand: ')))
            package_2nd = struct.pack('!i', int(input('2nd operand: ')))
            s.send(package_opc)
            s.send(package_1st)
            s.send(package_2nd)

        solution = s.recv(BUFFER_SIZE)

        if package_opc == 1:
            print('The solution is: ', solution)
        else:
            print('The solution is: ', struct.unpack('!i', solution)[0])

    s.close()

if __name__ == "__main__":
    main()