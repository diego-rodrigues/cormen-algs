# -*- coding: utf-8 *-*

def _partition(A, p, r):
    """ Partition method for quicksort. """
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            aux = A[j]
            A[j] = A[i]
            A[i] = aux
    i += 1
    aux = A[r]
    A[r] = A[i]
    A[i] = aux
    return i

def quicksort(A, p, r):
    """ 
    Quicksort algorithm. It receives the array A, the first and last
    indexes p and r.
    """
    if p < r:
        q = _partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

if __name__ == "__main__":
    uns_array_1 = [5,3,10,8,9,2,4,1]
    uns_array_2 = [0,0,1,1,2,0,1]

    print(uns_array_1)
    quicksort(uns_array_1, 0, len(uns_array_1)-1)
    print(uns_array_1)

    print(uns_array_2)
    quicksort(uns_array_2, 0, len(uns_array_2)-1)
    print(uns_array_2)