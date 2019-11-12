# -*- coding: utf-8 *-*

import unittest
from max_subarray_dc import max_subarray
from max_subarray_kadanes import max_subarray_kadanes

# test array 
# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
A = [1]
# solution
# sol_A = (43, 7, 10)
sol_A = (1, 0, 0)

class TestMaxSubarray(unittest.TestCase):
    """ class for testing max subarray problem """
    def test_max_subarray_dc(self):
        self.assertEqual(max_subarray(A, 0, len(A)-1), sol_A)

    def test_max_subarray_kadanes(self):
        self.assertEqual(max_subarray_kadanes(A, 0, len(A)-1), sol_A)

if __name__ == "__main__":
    unittest.main()