#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket
import sys


def main(argv):
    IP = ''  # listens to every sending IP, for security enter client IP
    PORT = 50050
    BUFFER_SIZE = 1400

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break

    conn.close()


if __name__ == "__main__":
    main()