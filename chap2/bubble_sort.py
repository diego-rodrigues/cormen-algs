# -*- coding: utf-8 *-*

def bubble_sort(A):
    """ Sorts an array A via bubblesort algorithm. """
    for i in range(0,len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j] < A[j-1]:
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
    return A
