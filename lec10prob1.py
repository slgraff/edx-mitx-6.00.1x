# lec10prob1.py
#
# Answers to questions are answered online. Definitions and questions
# included here to help understand problems.

# In this problem, we'll examine how indirection works.
# Consider the following definitions:

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

# 1. What is the value of the following expressions? If you think
# there will be an error, please type in 'error' (without quotes)
# in the input box.

# I've wrapped them in print() statements to show values

print(a[0])
print(b[1])
print(a[a[1]])
print(b[b[2]])
print(a[b[2]])
print(c[a[b[3]]])
print(a[c[a[b[0]]]])
print(a[c[a[b[3]]]])

# 2. Assume we have defined the following function:

def foo(L):
    val = L[0]
    while (True):
        val = L[val]

# Which of the following statement(s) will result in an infinite loop?

print(foo(a))
print(foo(b))
print(foo(c))

# 3. Consider the following code:

# Note that this code will not run as-s with num is set to '???'
# Commented it out and included lines for each possible value.
# Comment out desired assignment for num to run
# num = ???
num = 0
# num = 1
# num = 3
# num = 5
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val

#   1) What is the smallest value that num can be such that the number 3 is printed?
#           0
#           1
#           3
#           5
#           Impossible


#   2) Now, we redefine L to be:

L = [2, 0, 1, 5, 3, 4]

#       What is the smallest value that num can be such that the number 3 is printed?
#           0
#           3
#           5
#           Impossible
