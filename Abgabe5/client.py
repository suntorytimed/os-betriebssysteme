#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
"""

@author: Stefan Weiberg, Jan Opitz, Jennifer Liebel
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
            break
        elif operation in QUIT:
            return 0
        else:
            print('Invalid input, try again!')

    return package_operation


def main():
    IP = input('Enter the server IP: ')
    PORT = eval(input('Enter the connection port: '))
    BUFFER_SIZE = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while(True):
        package_opc = input_operation()
        package = bytes(package_opc)
        print (package)

        if package_opc == 0:
            break
        elif package_opc[0] == 2:
            package += (input('1st operand: ')).encode('utf-8')
            package += (input('2nd operand: ')).encode('utf-8')
        else:
            package += (struct.pack('!i', int(input('1st operand: '))))
            package += (struct.pack('!i', int(input('2nd operand: '))))

        s.sendall(package)

        solution = s.recv(BUFFER_SIZE)

        if package_opc[0] == 2:
            print('The solution is: ', solution.decode('utf-8'))
        else:
            print('The solution is: ', struct.unpack('!i', solution)[0])

    s.close()

if __name__ == "__main__":
    main()