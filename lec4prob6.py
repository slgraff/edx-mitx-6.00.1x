# lec4prob6.py
# Code for Lecture 4, Problem 6
#
# Below is a transcript of a session with the Python shell.
# Provide the type and value of the expressions being evaluated.
# If evaluating an expression would cause an error, select NoneType
# and write 'error' in the box. If the result is a function, select
# function and write 'function' in the box.
#
# To get the most out of this problem, try to figure out the answers
# by reading the code, not running it. Run the code in your interpreter
# only after you've checked your answers a few times.

# Entering this info a it's own python file for practice in order to
# re-enforce the concepts presented.
# Remove comments from either 1 or 2 to test
# I've wrapped the function calls in a print statement to make it easier
# to see the result


# Transcript 1
# a = 10
# def f(x):
#     return x + a
# a = 3
# print str(f(1))

# Transcript 2
# Note, I cannot get this code to run in IDLE or Canopy IDE's
# I always get error 'IndentationError: unexpected indent' but
# according to approved answer I should be getting '19'
x = 12
def g(x):
    x = x + 1
        def h(y):
            return x + y
        return h(6)
g(x))
