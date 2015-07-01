# lec5.7-towerOfHanoi.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 7

# Towers of Hanoi
# Example of problem that is easy to solve using recursion, but hard
# to solve interatively
#
# Have three tall spikes
# Stack of 64 different sized discs on one spikes
# Need to move them to to other spike, but can only move
# one at a time, and cannot put disc on top of smaller one

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

# Examples of calling Towers()
Towers(1, 'f', 't', 's')
Towers(2, 'f', 't', 's')
Towers(5, 'f', 't', 's')
