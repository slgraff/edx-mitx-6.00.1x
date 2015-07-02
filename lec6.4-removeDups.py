# lec6.4-removeDups.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, video 4

# Demonstrates performing operations on lists

# Demonstrates how changing a list while iterating over it creates
# unintended problems
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            # Note: we are iterating over L1, but just removed one of
            # its elements
            L1.remove(e1)
            # L1 is now [2,3,4] so when it loops through again the next
            # element is 3. As a result the 2 is skipped and not removed
            # as intended


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)

# Better way to perform operations on list by creating a copy of L1
# then iterating over that as it will not change
def removeDupsBetter(L1, L2):
    # Make a copy of L1 and put into L1Start
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)
