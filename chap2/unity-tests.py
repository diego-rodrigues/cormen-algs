# -*- coding: utf-8 *-*

import unittest
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort


# unsorted array for testing and answers
uns_array_1 = [5,3,10,8,9,2,4,1]
ans_array_1 = [1,2,3,4,5,8,9,10]

uns_array_2 = [0,0,1,1,2,0,1]
ans_array_2 = [0,0,0,1,1,1,2]

class TestSort(unittest.TestCase):
    """ class for sorting algorithms """
        
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(uns_array_1), ans_array_1,
            "Should be " + str(ans_array_1))

    def test_insertion_sort_rep(self):
        self.assertEqual(insertion_sort(uns_array_2), ans_array_2,
            "Should be " + str(ans_array_2))

    def test_selection_sort(self):
        self.assertEqual(selection_sort(uns_array_1), ans_array_1,
            "Should be " + str(ans_array_1))

    def test_selection_sort_rep(self):
        self.assertEqual(selection_sort(uns_array_2), ans_array_2,
            "Should be " + str(ans_array_2))

    def test_merge_sort(self):
        self.assertEqual(
            merge_sort(uns_array_1,0,len(uns_array_1)-1), 
            ans_array_1,
            "Should be " + str(ans_array_1))

    def test_merge_sort_rep(self):
        self.assertEqual(
            merge_sort(uns_array_2,0,len(uns_array_2)-1), 
            ans_array_2,
            "Should be " + str(ans_array_2))

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(uns_array_1), ans_array_1,
            "Should be " + str(ans_array_1))

    def test_bubble_sort_rep(self):
        self.assertEqual(bubble_sort(uns_array_2), ans_array_2,
            "Should be " + str(ans_array_2))
        
if __name__ == "__main__":
    unittest.main()
