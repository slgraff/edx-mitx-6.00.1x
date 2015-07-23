# lec10prob4.py


# In lecture, we saw a version of linear search that used the fact that a statements
# of elements is sorted in increasing order. Here is the code from lecture:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# Consider the following code, which is an alternative version of search.
# search3 recursively calls itself
def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

# Which of the following statements is correct? You may assume that each
# function is tested with a list L whose elements are sorted in increasing
# order. For simplicity, assume L is a list of integers.

# - search and search3 return the same answers
# - search and search3 return the same answers provided L is non-empty
# - search and search3 return the same answers provided L is non-empty and e is in L
# - search and search3 do not return the same answers
# - search and search3 return the same answers for lists of length 0 and 1 only

# Sample list and calls to both search and search3 with different lists
# to match conditions in above possible answers

# Search for a number in list
print(search([2, 5, 7, 10, 15, 27, 35, 44], 35))
print(search3([2, 5, 7, 10, 15, 27, 35, 44], 35))
print

# Search for a number not in list
print(search([2, 5, 7, 10, 15, 27, 35, 44], 3))
print(search3([2, 5, 7, 10, 15, 27, 35, 44], 3))
print

# Search for a number in an empty list
print(search([], 5))
print(search3([], 5))
print

# Search for a number in a single element list
print(search([5], 5))
print(search3([5], 5))
print
