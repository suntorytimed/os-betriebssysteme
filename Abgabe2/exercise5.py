#!/usr/bin/python -Es
from threading import Thread

counter = 0

def minus():
  global counter
  for i in range(1000):
    counter -= 1

def plus():
  global counter
  for i in range(1000):
    counter += 1

threads = []
  
for i in range(5):
  thread = Thread(target = minus)
  threads += [thread]
  thread.start()
  thread = Thread(target = plus)
  threads += [thread]
  thread.start()
    
for thread in threads:
  thread.join()
  print "Thread Nr. %d joined." % thread.ident

print counter
