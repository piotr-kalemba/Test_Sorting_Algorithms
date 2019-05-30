import unittest
import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def partition(a, start, end):

    pivot = a[end]
    first_high = start

    for i in range(start, end):

        if a[i] < pivot:
            swap(a, i, first_high)
            first_high += 1

    swap(a, first_high, end)

    return first_high

def quick_sorting(a, start, end):

    if start < end:

        pivot_index = partition(a, start, end)

        quick_sorting(a, start, pivot_index - 1)
        quick_sorting(a, pivot_index + 1, end)


def quick_sort(a):

    quick_sorting(a, 0, len(a) - 1)


# below we run a unittest to make sure if quick_sort indeed sorts a random list:

random_list = []

for _ in range(100):

    draw = random.randint(0,1000)
    random_list.append(draw)

random_list_copy = random_list[:]

quick_sort(random_list)

random_list_copy.sort()

class TestQuickSort(unittest.TestCase):

    def test_1(self):

        self.assertEqual(random_list, random_list_copy)


if __name__ == '__main__':
    unittest.main()