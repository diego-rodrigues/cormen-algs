# -*- coding: utf-8 *-*

# Kadanes algorithm to find the maximum subarray sum
def max_subarray_kadanes(A, low, high):
    """
    Finds the maximum sum in subarray. Follows the Kadanes algorithm.
    """
    max_sum = 0
    max_low = -1
    max_high = -1
    total_sum = 0
    starting_i = 0

    for i in range(low, high+1):
        total_sum += A[i]

        if total_sum > max_sum:
            max_sum = total_sum
            max_high = i
            max_low = starting_i

        if total_sum < 0:
            total_sum = 0
            starting_i = i+1

    return (max_sum, max_low, max_high)
