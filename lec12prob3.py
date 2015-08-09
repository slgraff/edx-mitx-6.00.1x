# lec12prob3.py
#
# Lecture 12 - Object Oriented Programming
# Problem 3
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

"""
In this problem, you'll be asked to read through an object-oriented
implementation of the hand from the word game problem of Problem Set 4. You'll
then be asked to implement one of its methods. Note that the implementation
of the object-oriented version of the hand is a bit different than how we did
things with the functional implementation; pay close attention to doc strings
and read through the implementation carefully.

To begin: Download L12_hand.py and read through the file. Be sure to understand
what's going on in the file. Make a few instances of the Hand class, and play
around with the existing methods.

When you have completed reading through the file, implement the update method.

Paste the entire Hand class in the box below.

The __str__ method is this:

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

"""
