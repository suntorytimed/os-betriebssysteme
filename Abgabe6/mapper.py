#!/usr/bin/python -Es
# -*- coding: utf-8 -*-
import mmap


def loop(mm):
    while True:
        for j in range(100):
            mm.write('A')
        mm.write('\n')

with open("testfile.test", "wb") as out:
    out.truncate(1024 * 1024)

with open("testfile.test", "r+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print mm.size()

    try:
        loop(mm)
    except ValueError:
        print "Write to file finished."

    mm.flush()
    mm.close()