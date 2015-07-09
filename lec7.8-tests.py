# lec7.8-tests.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 7, video 8
# Debugging as Search

# Used in lecture to demonstrate using binary search method to find bug in code
# For this code, when testing for 'ab', the program erroneously says that this
# is a palindrome. We need to find out why this is occurring. 

# I've noted the debugging steps using 1st, 2nd, 3rd... to note the order of the
# performed debugging steps

def isPal(x):
    assert type(x) == list
    # 5th - after fixing below line, code works correctly
    temp = x[:]
    # 4th - insert print statment here
    # Result is still the same, problem is determined to be with reverse
    # Did not invoke correctly, should be temp.reverse()
    print (temp, x)

    # Fixed this to invoke correctly, but still now both temp and x
    # getting reversed. temp is a pointer (alias) of x, need to
    # change to temp = x[:]
    temp.reverse()
    # 3rd - insert print statement here
    # Result is that temp and x are both ['a', 'b']
    print (temp, x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        # Below is initializing result each time through loop
        # Move it above the for loop so only initialized once
        # result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
        # 2nd - insert a print statemnt inside the print loop to further test
        # Result is that inputs still being dropped
        print (result)
    # 1st - insert a print statement about mid-way thorugh to help in debugging
    # Result shows that the list is dropping inputs
    print (result)
    if isPal(result):
        print('Yes')
    else:
        print('No')


# Examples of calling silly(n), where n is number of test cases
# silly(5) # enter 'abcba'
# silly(10) # enter 'palinnilap'
silly(2) # enter 'ab'

