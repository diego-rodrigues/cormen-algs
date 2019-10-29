# -*- coding: utf-8 *-*

def _merge(A, p, q, r):
    """ Sorts an array A, part of the merge sort method. """

    if p == r:
        return A

    # creating left and right arrays
    L = A[p : q+1]
    R = A[q+1 : r+1]

    # merging
    i = 0
    j = 0
    for k in range(p,r+1):
        # checking for out of bounds elements
        if i == len(L):
            A[k] = R[j]
            j += 1
        
        elif j == len(R):
            A[k] = L[i]
            i += 1
        # checking for lowest value
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        
        else:
            A[k] = R[j]
            j += 1

    return A

def merge_sort(A, p, r):
    """ Executes the mergesort algorithm. 
        Watch out for figuring out indexes, can be janky when starting on 0.
        P is zero and R is the maximum index, then its len(A) - 1.
    """
    if p < r:
        q = (int)((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        _merge(A, p, q, r)
    return A