# lec10.4-selection_sort.py
# Lecture 10, video 4

# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

# What about cost of sorting?
# Assume complexity of sorting a list is O(sort(L))
# If we sort and search we want to know if
# sort(L) + log(len(L)) < len(L)
#   - i.e. should we sort and search using binary,
#    or just use linear search
# Can't sort in less than linear time, sort is at least the complexity
# of performing a linear search

# What about searching a list k times?
# Is sort(L) + k*log(len(L)) < k*len(L)?
#   - Depends on k, but expectation if sort can be done
#   efficiently then is better to sort first
#   - Amortizing cost of sorting over multiple searches
#   may make this worthwhile

# Selection Sort function to go through and sort a list
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp

# Analysis of select sort complexity
#   Inner while loop is O(len(L))
#   Outer loop also O(len(L))
#   Overall complexity is O(len(L)**2), or quadratic
#   i.e. is expensive
