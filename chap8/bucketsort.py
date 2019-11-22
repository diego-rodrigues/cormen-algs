# -*- coding: utf-8 *-*

import sys
import math
sys.path.append("./")
from chap2.insertion_sort import insertion_sort

def _bucketsort(A):
    """ 
    Implements the bucket sort algorithm. Uses insertion sort as the 
    auxiliar sorting method. It assumes all values in A are between (0,1).
    """
    B = []

    # creating buckets
    for i in range(0, len(A)):
        empty = []
        B.append(empty)

    # put elements in buckets
    for i in range(0, len(A)):
        bucket_index = (int)(A[i] * len(A))
        B[bucket_index].append(A[i])

    # sort buckets using insertion sort
    # copies sorted bucket to final array
    C = []
    for i in range(0, len(A)):
        bucket = B[i]
        insertion_sort(bucket)
        for element in bucket:
            C.append(element)

    return C

def bucketsort(A):
    """
    A modifier so bucketsort runs on sets with values out of [0,1).
    """
    maximum = max(A)
    multiplier = (int)(math.log10(maximum)) + 1
    multiplier = math.pow(10.0, multiplier)
    A = [a/multiplier for a in A]
    A = _bucketsort(A)
    A = [(int)(a*multiplier) for a in A]
    return A

if __name__ == "__main__":
    uns_array_1 = [5,3,14,8,9,2,4,1]
    uns_array_2 = [0,0,1,1,2,0,1]

    print(uns_array_1)
    uns_array_1 = bucketsort(uns_array_1)
    print(uns_array_1)

    print(uns_array_2)
    uns_array_2 = bucketsort(uns_array_2)
    print(uns_array_2)
