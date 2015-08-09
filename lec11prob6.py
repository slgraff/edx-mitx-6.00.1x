# lec11prob6.py
#
# Lecture 11 - Classes
# Problem 6
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

'''
For this exercise, you will be coding your very first class, a 'Queue' class.
Queues are a fundamental computer science data structure. A queue is basically
like a line at Disneyland - you can add elements to a queue, and they maintain
a specific order. When you want to get something off the end of a queue, you
get the item that has been in there the longest (this is known as
'first-in-first-out', or FIFO). You can read up on queues at Wikipedia if you'd
like to learn more.

In your Queue class, you will need three methods:

    1. __init__: initialize your Queue (think: how will you store the queue's
    elements? You'll need to initialize an appropriate object attribute in
    this method)

    2. insert: inserts one element in your Queue

    3. remove: removes (or 'pops') one element from your Queue and returns it.
    If the queue is empty, raises a ValueError.

When you're done, you should test your implementation.
'''

class Queue (object):
    def __init__(self):
        self.vals = []

    def insert(self, a):
        self.vals.append(a)

    def remove(self):
        try:
            the_result = self.vals.pop(0)
        except ValueError:
            raise ValueError()
        else:
            return the_result


# calles to Queue for testing
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
