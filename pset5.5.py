# pset5.5.py

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


# Sample list and calls to both search and search3 with different lists
# to match conditions in above possible answers

# Search for a number in list
print(search([2, 5, 7, 10, 15, 27, 35, 44], 35))
print(newsearch([2, 5, 7, 10, 15, 27, 35, 44], 35))
print

# Search for a number not in list
print(search([2, 5, 7, 10, 15, 27, 35, 44], 3))
print(newsearch([2, 5, 7, 10, 15, 27, 35, 44], 3))
print

# Search for a number in an empty list
print(search([], 5))
print(newsearch([], 5))
print

# Search for a number in a single element list
print(search([5], 5))
print(newsearch([5], 5))
print
