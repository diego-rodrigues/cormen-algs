# -*- coding:utf-8 -*-

def countsort(A):
    """ 
    Runs the sorting by counting. It receives the array A.
    """
    k = max(A)
    C = [0] * (k+1)
    B = [''] * len(A)
    for i in range(0, len(A)):
        C[A[i]] += 1
    
    for j in range(1, k+1):
        C[j] += C[j-1]
    
    for i in range(len(A)-1, -1, -1):
        # this for goes to the last to the first element of A
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B

if __name__ == "__main__":
    uns_array_1 = [5,3,10,8,9,2,4,1]
    uns_array_2 = [0,0,1,1,2,0,1]

    print(uns_array_1)
    uns_array_1 = countsort(uns_array_1)
    print(uns_array_1)

    print(uns_array_2)
    uns_array_2 = countsort(uns_array_2)
    print(uns_array_2)