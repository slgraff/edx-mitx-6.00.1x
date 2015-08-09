# sharp.py
# Sharp - Practice Question
# This practice question has been created by Nitish Mittal (Teaching Assistant)
# for course MITx 6.00.1x Summer 2015 on edX. This is in reference to week 3
# course material.
#
# You must have heard about factorial (5!), square root(root 5), etc of a number.
# Let us assume there exists an operation “#” on integers greater than equal to 2
# such that for any integer x >= 2,
#
# x# = ((((((2 ^ 3) ^ 4) ^ 5)  …)  …)     x-1) ^  x)
#
# For example ->
# 2# = 2
# 3# = (2 ^ 3) = 8
# 4# = ((2 ^ 3) ^ 4) = (8 ^ 4) = 4096
#
# Write a function “sharp(x)” that takes an integer ‘x’ as argument and gives
# out the value of x#.
#
# Suppose num_digits(x) represents the number of digits in the integer x,
# give the value of "result" where,
#
# result = num_digits(7#) + 2 * num_digits(6#) + num_digits(5#) + num_digits(4#)
