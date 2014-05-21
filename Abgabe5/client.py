#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author: Jennifer Liebel, Stefan Weiberg, Jan Opitz
"""

import socket
import sys


def standard_package(size):
    package = bytearray()
    package.append(int_input())
    package.append(int_input())


def main(argv):
    IP = "127.0.0.1" #enter server IP
    PORT = 5005
    PACKAGE = standard_package(1400)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    #i = 0
    #while i < number_packages:
	#if split:
	    #if i%n == 0:
		#time.sleep(k)
	#s.send(PACKAGE)
	#if first_time:
	    #start_time = time.time()
	    #first_time = False
	#else:
	    #last_time = time.time()
	#i+=1
    s.close()

        #time_diff = last_time-start_time
        #throughput = (number_packages * 11.2) / time_diff
        #print "Senderate = %f KBit/s" % throughput


if __name__ == "__main__":
    main()
