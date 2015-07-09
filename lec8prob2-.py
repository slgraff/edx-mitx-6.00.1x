# lec8prob2-.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 8, problem 2

# Below are some short Python programs. For each program, answer the
# associated question.
#
# Try to answer the questions without running the code. Check your answers,
# then run the code for the ones you get wrong.
#
# The function in the following questions takes a list of integers numbersand
# a position index, and divides each entry in the list of numbers by the value
# at entry index.

# There are five functions named FancyDivide. Uncomment the one you wish to
# use along with the calls to it to test

# def FancyDivide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError, e:
#         print "-1"
#     else:
#         print "1"
#     finally:
#         print "0"


# def FancyDivide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError, e:
#         FancyDivide(numbers, len(numbers) - 1)
#     except ZeroDivisionError, e:
#         print "-2"
#     else:
#         print "1"
#     finally:
#         print "0"


def FancyDivide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"


# def FancyDivide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception, e:
#         print e


# def FancyDivide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception, e:
#         print e

# Calls to FancyDivide
# FancyDivide([0, 2, 4], 1)
print ''
FancyDivide([0, 2, 4], 4)
print ''
# FancyDivide([0, 2, 4], 0)
