#!/usr/bin/python -Es
print "Bello World!"

def Hello():
  print "Hello Word!"

Hello()

class World:
  def __init__(self):
    pass

  def HelloWorld(self):
    print "Hello World!"

helloWorld = World()
helloWorld.HelloWorld()

for x in range(10):
  print str(x+1) + " Hello World!"
