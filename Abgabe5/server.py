#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket
from threading import Thread

clients = []
IP = ''  # listens to every sending IP, for security enter client IP
PORT = 50050
BUFFER_SIZE = 1400


class client:

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        global BUFFER_SIZE

        data = []

        while True:

            data += [self.conn.recv(BUFFER_SIZE)]
            #if not data:
                #break
            if data.length == 3:
                if data[0] == '+':
                    self.conn.send(data[1] + data[2])
                elif data[0] == '*':
                    self.conn.send(data[1] * data[2])
                elif data[0] == '#':
                    self.conn.send(data[1].append(data[2]))
                data = []

        self.conn.close()


def main(argv):
    global clients
    global IP
    global PORT
    global BUFFER_SIZE

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    clients += [client(conn, addr)]


if __name__ == "__main__":
    main()