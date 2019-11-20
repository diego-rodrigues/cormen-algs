# -*- coding: utf-8 *-*

import math
from heapsort import max_heapify, _parent

def heap_maximum(A):
    """ Gets the maximum value of a heap. """
    try:
        return A[0]
    except:
        return None

def heap_extract_max(A):
    """ Gets the maximum value of a heap and removes it from the heap. """
    if len(A) > 0:
        maximum = A[0]
        try:
            del A[0]
            max_heapify(A, 0,  len(A))
        except:
            A = []
        return maximum
    else:
        return None

def heap_increase_key(A, i, key):
    """ 
    Increases the value at A[i] to key. If key is lower than the
    value at A[i], the operation fails.
    """
    if key < A[i]:
        return None

    A[i] = key
    while (i > 0) and (A[_parent(i)] < A[i]):
        aux = A[_parent(i)]
        A[_parent(i)] = A[i]
        A[i] = aux
        i = _parent(i)

def max_heap_insert(A, key):
    """ Inserts a new key into the maximum heap A. """
    A.append(-math.inf)
    heap_increase_key(A, len(A)-1, key)

def max_heap_delete(A, i):
    """ Deletes the ith element from the maximum heap A. """
    heap_increase_key(A, i, math.inf)
    del A[0]
    max_heapify(A, 0, len(A))


if __name__ == "__main__":
    A = [5,3,10,8,9,2,4,1]
    print('array: ', A)

    from heapsort import build_max_heap
    build_max_heap(A)
    print('heap: ', A)
    print('maximum value heap: ', heap_maximum(A))

    heap_extract_max(A)
    print('heap after extract max value: ', A)

    heap_increase_key(A, 3, 15)
    print('increased key 3 to 15: ', A)

    max_heap_insert(A, 11)
    print('inserted key 11: ', A)

    max_heap_delete(A, 4)
    print('deleted element at 4: ', A)

    max_heap_delete(A, 0)
    print('deleted element at 0: ', A)