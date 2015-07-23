# pset5.6-3-swapSort.py

# If we make a small change to the line for j in range(i+1, len(L)):
# such that the code becomes:

def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L


modSwapSort([1,9,2,8,3,7,4,6,5])
modSwapSort([5, 9, 4])
