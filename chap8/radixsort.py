# -*- coding:utf-8 -*-

def _stable_sort(A, divider):
    """ Any stable sorting algorithm will do. This is count sort. """

    # counters from 0 to 9
    C = [0] * 10
    # auxiliar array with sorted values
    B = [0] * len(A)

    # count digits appearences
    for i in range(0, len(A)):
        digit = A[i] / divider
        digit = (int)(digit % 10)
        C[digit] += 1

    # counting positions
    for i in range(1, 10):
        C[i] += C[i-1]

    # creates sorted array by the considered digit
    for i in range(len(A)-1, -1, -1):
        digit = A[i] / divider
        digit = (int)(digit % 10)
        B[C[digit]-1] = A[i]
        C[digit] -= 1
    return B


def radixsort(A):
    """ Implements sorting by digits -- radixsort. """
    maximum = max(A)
    divider = 1
    while maximum/divider >= 1:
        A = _stable_sort(A, divider)
        divider *= 10
    return A

if __name__ == "__main__":
    uns_array_1 = [5,3,10,8,9,2,4,1]
    uns_array_2 = [0,0,1,1,2,0,1]

    print(uns_array_1)
    uns_array_1 = radixsort(uns_array_1)
    print(uns_array_1)

    print(uns_array_2)
    uns_array_2 = radixsort(uns_array_2)
    print(uns_array_2)