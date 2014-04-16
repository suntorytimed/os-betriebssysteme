#!/usr/bin/python -Es
import os

def process():
  childs = []

  for i in range(3):
  
    newpid = os.fork()
    childs += [newpid]
   
    if newpid == 0:
      for j in range(200):
        print "Kind mit PID = ", os.getpid() 
 
  for k in range(200):
     
    index = 1

    for child in childs:  
      print "child %d: %d" % (index, child)
      index += 1
    print ""

process()

os._exit(0)
