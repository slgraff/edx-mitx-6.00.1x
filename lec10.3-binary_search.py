# lec10.3-binary_search.py
# Binary Search

# Can we do better than O(len(L)) for search?
# If know nothing about values of elements in list, then no
# Worst case have to look at every values

# What if list is ordered? Suppose elements are sorted?
# Example of searching an ordered list
def search(L, e):
    for i in range (len(L)):
        if L[i] == e:
            return True
        # if element in list is bigger than item looking for,
        # know that element is not in an ordered list, return False
        # Improves complexity, but worst case still need to look at
        # every element
        if L[i] > e:
            return False
    return False

# Use binary search to create a divide and conquer algorithm
# Pick an index i that divides list in half
#   if L[i] == e, then found value
#   If not, ask if L[i] larger or smaller, set to new i

def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == c
        mid = low + int((high - low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            # Incorrect line from slides, corrected below
            # return bSearch(L, e, low, mid - 1)
            # If value we are seaching for is less than curent value,
            # set a new range from low to mid
            return bSearch(L, e, low, mid)
        else:
            # Otherwise, if value search for is higher, then a new
            # range from mid + 1 (so we don't look at same value again, to high)
            return bSearch(l, e, mid + 1, high)

    # If list is empty, return False
    if len(L) == 0:
        return False
    # Otherwise, call bSearch, low = 0, high set to len(L) - 1
    else:
        return bSearch(L, e, 0, len(L) - 1)

"""
Analyzing binary search
    Does the recursion halt?
        - Decrementing function
        1. Maps values to which formal parameters are bound to
            non-negative integer
        2. When value <= 0, recursion terminates
        3. For each recursive call, value of function is strictly less then
            value on entry to instance of function
        - Here function is high - low
            - At least 0 first time called (1)
            - When exactly 0, no recursive calls, returns (2)
            - Otherwise, halt or recursively call with value halved (3)

    What is complexity?
        - How many recursive calls? (work within each call
            is constant)
        - How many times can we divide high - 1ow in
            half before reaches 0?
        - log2 (high - low)
        - Thus search complexity is O(log(len(L)))

        Is a very efficient algorithm, much better than linear
"""
