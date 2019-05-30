import unittest
import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def bubble_sort(a):

    length = len(a)

    for i in range(length):
        for j in range(1, length-i):
            if a[j-1] > a[j]:
                swap(a, j-1, j)


# below we run a unittest to make sure if bubble_sort indeed sorts a random list:

random_list = []

for _ in range(100):

    draw = random.randint(0,1000)
    random_list.append(draw)

random_list_copy = random_list[:]

bubble_sort(random_list)

random_list_copy.sort()

class TestBubbleSort(unittest.TestCase):

    def test_1(self):

        self.assertEqual(random_list, random_list_copy)


if __name__ == '__main__':
    unittest.main()