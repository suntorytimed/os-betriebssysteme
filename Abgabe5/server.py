#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket
import sys


def main(argv):
    IP = '' #listens to every sending IP, for security enter client IP
    PORT = 5005
    BUFFER_SIZE = 1400
    value = 5
    old_data = bytearray()
    old_data.append(255)
    old_data.append(255)
    first_time = True
    start_time = 0
    last_time = 0
    wrong_packages = 0
    total_packages = -1
    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr

    while True:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	total_packages += 1
	if first_time:
	    start_time = time.time()
	    first_time = False
	else:
	    last_time = time.time()

    conn.close()


if __name__ == "__main__":
    main()