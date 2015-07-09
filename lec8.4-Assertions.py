# lec8.4-Assertions.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 8, video 4

# Introductoin to using assertions in defensive programming
# Use an assert statement to spot bugs early, easier to track down
# Not to be used in place of testing computation are as expected
# Use to check types of arguments, checking constraints on return values,

def avg(grades, weights):
    # These assert statements check the inputs
    assert not len(grades) == 0, "no grades data"
    assert len(grades) == len(weights), "wrong number grades"
    newgr = [convertLetterGrade(elt) for elt in grades] # elt = element
    result = dotProduct(newgr, weights)/len(newgr)

    # This assert checks the results to make sure that they are valid
    assert 0.0 <= result <= 100.0
    return result


# Examples of calling avg() to show assert errors being raised
myGrades = []
myWeights = []

print avg(myGrades, myWeights)
