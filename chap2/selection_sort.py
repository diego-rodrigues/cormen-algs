# -*- coding: utf-8 *-*

def selection_sort(A):
    """ Sorts an array A """

    for i in range(0, len(A)-1):
        pivot = i
        lower = A[pivot]
        for j in range(i+1, len(A)):
            if A[j] < A[pivot]:
                pivot = j
                lower = A[pivot]

        if pivot != i:
            aux = A[i]
            A[i] = A[pivot]
            A[pivot] = aux

    return A