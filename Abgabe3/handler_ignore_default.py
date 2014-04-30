#!/usr/bin/python -Es
import signal
import time

def main():
    while(True):
	    time.sleep(5)
    
def handler1(signum,frame):
    print "Signal angekommen: SIGINT!"

def handler2(signum,frame):
    print "Signal angekommen: SIGQUIT!"
    
    
signal.signal(signal.SIGINT, handler1)
signal.signal(signal.SIGQUIT, handler2)
signal.signal(signal.SIGILL, signal.SIG_IGN)
signal.signal(signal.SIGTRAP, signal.SIG_DFL)

main()
