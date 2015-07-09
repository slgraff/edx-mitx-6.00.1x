# lec8prob4-.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 8, problem 4

# Consider the function Normalize that takes as input a list of positive numbers
# numbers and returns a list of numbers that are a fraction of the maximum
# element in the list. Try to answer the questions without running the code.
# Check your answers, then run the code for the ones you get wrong. You'll
# learn the most this way, by figuring things out, instead of just running the
# code and reading off the answers.

def Normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

# def Normalize(numbers):
#     max_number = max(numbers)
#     assert(max_number != 0), "Cannot divide by 0"
#     for i in range(len(numbers)):
#         numbers[i]  /= float(max_number)
#         assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
#     return numbers


try:
      Normalize([0, 0, 0])
except ZeroDivisionError, e:
      print 'Invalid maximum element'
