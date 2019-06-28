import unittest
import random
from bubble_sort import bubble_sort
from select_sort import select_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort

random_list = []

keys_list = list(range(300))
random_list = random.choices(keys_list, k=100)

list_bubble = random_list[:]
list_select = random_list[:]
list_merge = random_list[:]
list_heap = random_list[:]
list_quick = random_list[:]
sorted_list = sorted(random_list)

class TestLists(unittest.TestCase):

    def test_lists(self):

            self.assertNotEqual(sorted_list, list_bubble)
            self.assertListEqual(list_heap, list_merge)
            self.assertIsNot(list_heap, list_merge)


class TestSortingAlgorithms(unittest.TestCase):


    def test_bubble(self):
        bubble_sort(list_bubble)
        self.assertListEqual(sorted_list, list_bubble)

    def test_select(self):
        select_sort(list_select)
        self.assertListEqual(sorted_list, list_select)

    def test_merge(self):
        merge_sort(list_merge)
        self.assertListEqual(sorted_list, list_merge)

    def test_heap(self):
        heap_sort(list_heap)
        self.assertListEqual(sorted_list, list_heap)

    def test_quick(self):
        quick_sort(list_quick)
        self.assertListEqual(sorted_list, list_quick)


if __name__ == '__main__':
    unittest.main()