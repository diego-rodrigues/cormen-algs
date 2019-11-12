# -*- coding: utf-8 *-*

# Divide and conquer version of the algorithm to 
# find the maximum subarray sum

def max_crossing_subarray(A, low, mid, high):
    """
    Finds the maximum sum subarray - crossing.
    """
    # finding the maximum subarray starting from the middle to the left
    left_sum = -999
    total = 0
    for i in range(mid, low-1, -1):
        total += A[i]
        if total > left_sum:
            left_sum = total
            left_low = i
    # finding the maximum subarray starting from the middle to the right
    right_sum = -999
    total = 0
    for i in range(mid+1, high+1):
        total += A[i]
        if total > right_sum:
            right_sum = total
            right_high = i
    return (left_sum + right_sum), left_low, right_high

def max_subarray(A, low, high):
    """
    Finds the maximum subarray. Divide and conquer version.
    """
    # base case: one element
    if low == high:
        return A[low], low, high
    # divide and conquer
    else:
        mid = (int)((low + high) / 2)
        # find max in left side
        left_sum, left_low, left_high = max_subarray(A, low, mid)
        
        # find max in right side
        right_sum, right_low, right_high = max_subarray(A, mid+1, high)

        # find max crossing middle
        cross_sum, cross_low, cross_high = \
            max_crossing_subarray(A, low, mid, high)

        # return the highest value
        if left_sum > right_sum and left_sum > cross_sum:
            return left_sum, left_low, left_high
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_sum, right_low, right_high
        else:
            return cross_sum, cross_low, cross_high

