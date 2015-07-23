# lec10.7-merge_sort.py
# Lecture 10, video 7

# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

# Selection sort is expensive as it's quadratic, need to find
# a better, less expensive method

# Merge sort uses a divide and conquer method
#   If list is of length of 0 or 1, already sorted
#   If more than one element, split into two lists and sort each
#   Merge the results

 # Example of merging lists
 #  Compare smallest elements of each list, move smallest into new list
 #  Continue above until one list is empty, at that point copy remaining
 #  elements in list to new list

 # Complexity of merge
 #  Comparison and copying are constant
 #  Number of comparisons O(len(L))
 #  Number of copyings O(len(L))
 # Merging is linear in length of list


 def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i]), right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

# Complexity of merge sort
# Merge is O(len(L))
# Mergesort is O(len(L)) * number of calls to merge
#   O(len(L)) * number of calls to Mergesort
#   O(len(L)) * log(len(L))
# Log linear - O(n log n) where n is len(L)
