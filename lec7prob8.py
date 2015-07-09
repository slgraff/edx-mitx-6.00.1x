# lec7prob8.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 7, problem 8

# Debug following code

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      # Problem is here, where n is equal to zero
      # Gets multiplied by previous results gving us 0
      # Need to return 1 instea
      return 1
   else:
      return n * f(n-1)

# When we call f(3) we expect the result 6, but we get 0.
print (f(3))

# When we call f(1) we expect the result 1, but we get 0.
print (f(1))

# When we call f(0) we expect the result 1, but we get 0.
print (f(0))
