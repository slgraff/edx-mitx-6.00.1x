# lab4.4-iterativePower.py
# Example of computation without and with functional abstraction

# Code example without functional abstraction

##x = raw_input('Enter a number: ')
##p = int(raw_input('Enter an integer power: '))
##
##result = 1
##
##for turn in range(p):
##    print('iteration: ' + str(turn) + ' current result: ' + str(result))
##    result = result * x


# Code with functional abstraction

def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

# Call the function iterativePower
z = iterativePower(3, 5)
print str(z)