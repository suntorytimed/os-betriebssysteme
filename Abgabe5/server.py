#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
"""

@author: Stefan Weiberg, Jan Opitz, Jennifer Liebel
"""

import socket
import os
import struct


IP = ''  # listens to every sending IP, for security enter client IP
PORT = 50050
BUFFER_SIZE = 4096


class client:

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def run(self):
        global BUFFER_SIZE

        while True:
            data = self.conn.recv(BUFFER_SIZE)
            print(data)
            if not data:
                break
            elif data[0] != 2:
                first = data[1:5]
                second = data[5:9]
                first_int = struct.unpack('!i', first)
                second_int = struct.unpack('!i', second)
                print(first_int[0])
                print(second_int[0])
                if data[0] == 0:
                    self.conn.send(struct.pack('!i', first_int[0] + second_int[0]))
                elif data[0] == 1:
                    self.conn.send(struct.pack('!i', first_int[0] * second_int[0]))
            else:
                print(data[1:])
                print(data[0:])
                self.conn.sendall(data[0:])


def main():
    global IP
    global PORT
    global BUFFER_SIZE

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
    s.bind((IP, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        if os.fork():
            conn.close()
        else:
            conn_client = client(conn, addr)
            conn_client.run()
            conn.close()
            exit(0)


if __name__ == "__main__":
    main()