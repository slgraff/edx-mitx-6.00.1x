# lec10.2-search_algorithms.py
# Lecture 10 - Search Algorithms
# Search Algorithm - method for finding an item or group of items
# with specific properties within a collection of items
# Collection is called the search space

# Simple search method
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

# Complexity, if element not in list, O(len(L))
# At best is linear in length of L
# For list of objects of arbitrary size can
# use Indirection. Search is linear.
# Indirection - accessing something by first accessing something
# else that contains a reference to the thing sought.
