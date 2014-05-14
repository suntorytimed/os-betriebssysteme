#!/usr/bin/python -Es
from threading import Thread
import time
import argparse

#parse arguments
parser = argparse.ArgumentParser(description='synchronization demo')

parser.add_argument('-s', '--students', type=int,
                    help="number of students")
parser.add_argument('-t', '--time', type=int,
                    help="time for read action")
parser.add_argument('-r', '--return', type=int,
                    help="return timer")

args = parser.parse_args()

#global variables
read_time = args[1]
number_of_students = args[0]
return_timer = args[2]

books = []


def main():
    global books
    global number_of_students
    books += [book(1), book(1), book(1), book(2), book(2), book(3), book(3)]
    students = []

    for i in number_of_students:
        students += [student()]

if __name__ == "__main__":
    main()


class book:
    def __init__(self, param):
        self.book_name = param
        self.is_in_use = False


class student:

    def __init__(self):
        self.has_books = []
        self.counter = 0
        thread = Thread(target=self.studies)
        thread.start()

    def studies(self):
        global books
        global read_time
        global return_timer

        for i in books:
            if not i.is_in_use:
                has_book = False
                for j in self.has_books:
                    if i.book_name == j.book_name:
                        has_book = True
                if not has_book:
                    self.has_books += i
                    i.is_in_use = True

        self.counter += 1

        if len(self.has_books) == 3:
            time.sleep(read_time)
            print ("I read")
            self.give_back()

        if self.counter == return_timer:
            self.give_back()

    def give_back(self):
        for i in self.has_books:
            i.is_in_use = False
        self.has_books = []