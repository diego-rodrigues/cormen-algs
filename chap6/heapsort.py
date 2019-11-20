# -*- coding: utf-8 *-*

def _parent(i):
    """ Gets the index of the ith element of a heap. """
    return (int)((i - 1) / 2)

def _left(i):
    """ Gets the index of the left child of an ith element of a heap. """
    return (int)(2 * i + 1)

def _right(i):
    """ Gets the index of the right child of an ith element of a heap. """
    return (int)(2 * i + 2)

def max_heapify(A, i, length):
    """
    Max heapify operation. For a given array A, makes sure that the
    ith element satifies the heap condition.
    """
    l = _left(i)
    r = _right(i)

    if l < length and A[l] > A[i]:
        high = l
    else:
        high = i

    if r < length and A[r] > A[high]:
        high = r

    if high != i:
        aux = A[i]
        A[i] = A[high]
        A[high] = aux
        max_heapify(A, high, length)

def build_max_heap(A):
    """
    Creates a max heap.
    """
    half = (int)(len(A) / 2)
    for i in range(half, -1, -1):
        max_heapify(A, i, len(A))

def heapsort(A):
    """
    Sorts an array A according to heapsort method.
    """
    length = len(A)
    build_max_heap(A)
    for i in range(length-1, 0, -1):
        aux = A[i]
        A[i] = A[0]
        A[0] = aux
        length -= 1
        max_heapify(A, 0, length)

if __name__ == "__main__":
    A = [5,3,10,8,9,2,4,1]
    A = [0,0,1,1,2,0,1]
    print(A)
    heapsort(A)
    print(A)