#!/usr/bin/python -Es
from io import open

passwd = open("/etc/passwd", "r")

for line in passwd:
  substring = line.split(":")
  print "Username: " + substring[0]
  print "User-ID: " + substring[2]

passwd.close()
