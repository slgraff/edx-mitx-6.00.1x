# lec11prob2.py
#
# Lecture 11 - Classes
# Problem 2
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

# 1. Consider the following code.
# What does the code print out?
# Note difference between time and self.time

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print self.time

clock = Clock('5:30')
clock.print_time()

# 2. Consider the following code.
# What does the code print out?

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print time

clock = Clock('5:30')
clock.print_time('10:30')


# 3. Consider the following problem.
# What doe the code print out?
# Are boston_clock and paris_clock different objects?

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
