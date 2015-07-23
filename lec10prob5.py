# lec10prob5.py
# Lecture 10, problem 5

# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

# Here is the code for selection sort. For simplicity, assume L is
# a list of integers:

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

# And here is a suggested alternative:

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

# Calling selSort with list
# rawList = [1,9,2,8,3,7,4,6,5]
# print("List before sorting: \n" + str(rawList))
# selSort(rawList)
# print("List after sorting: \n" + str(rawList))

# Calling newSort with list
rawList = [1,9,2,8,3,7,4,6,5]
print("List before sorting: \n" + str(rawList))
newSort(rawList)
print("List after sorting: \n" + str(rawList))

# Questions:
#
# 1. Do these functions result in the same sorted lists?
#   Yes
#   No

# 2. Do these two functions execute the same number of assignments of values
# into entries of the lists?
#   Yes, they execute the same number of assignments.
#   No. newSort may use more - but never fewer - inserts than selSort.
#   No. selSort may use more - but never fewer - inserts than newSort.
#   No. Either function may use more inserts than the other.

# 3. Is the worst-case order of growth of these functions the same?
#   Yes. newSort and selSort have the same complexity.
#   No. newSort has higher complexity than selSort.
#   No. selSort has higher complexity than newSort.
