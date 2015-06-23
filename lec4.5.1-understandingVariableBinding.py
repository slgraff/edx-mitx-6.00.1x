# lec4.5.1-understandingVariableBinding.py
#
# In lecture following code was entered into interactive Python shell
# Entering it in a python file for further practice and to re-enforce
# understanding of subject matter

def f(x):
    y = 1
    x = x + y
    print("x = " + str(x))
    return x

x = 3
y = 2
z = f(x)

# When run in interactive shell it would then print 'x = 4'. Can also view
# values of variable by simply entering the name
# Including print statements in this file to show values
print "Value of z: " + str(z)
print "Value of x: " + str(x)
print "Value of y: " + str(y)

