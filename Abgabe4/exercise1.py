#!/usr/bin/python -Es
import time
import argparse
import threading
from threading import Thread

#parse arguments
parser = argparse.ArgumentParser(description='synchronization demo')

parser.add_argument('-s', '--students', type=int,
                    help="number of students")
parser.add_argument('-t', '--time', type=int,
                    help="time for read action")

args = parser.parse_args()

#global variables
read_time = args.time
number_of_students = args.students

books = []


class student:

    def __init__(self, number):
        self.could_read = 0
        self.thread = Thread(target=self.studies)
        self.thread.setName(number)
        self.thread.start()

    def studies(self):
        global books
        global read_time
        global usage
        counter = 0

        while(True):
            for i in books:
                i.acquire()

            time.sleep(read_time)
            self.could_read += 1
            counter += 1

            if counter == 20:
                print(("Student " + self.thread.getName() + " studies for the %i. time." % self.could_read))
                counter = 0

            for i in range(2, -1, -1):
                books[i].release()

            time.sleep(1)

def output(string):
    print(string)


def main():
    global books
    global number_of_students

    books += [threading.Semaphore(3), threading.Semaphore(2), threading.Semaphore(2)]
    students = []

    for i in range(number_of_students):
        students += [student(i + 1)]


if __name__ == "__main__":
    main()