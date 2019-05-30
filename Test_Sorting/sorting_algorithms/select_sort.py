import unittest
import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def select_sort(a):

    for i in range(len(a)):

        minimum = min(a[i:])
        j = i + a[i:].index(minimum)
        swap(a, i, j)

# below we run a unittest to make sure if select_sort indeed sorts a random list:

random_list = []

for _ in range(100):

    draw = random.randint(0,1000)
    random_list.append(draw)

random_list_copy = random_list[:]

select_sort(random_list)

random_list_copy.sort()

class TestSelectSort(unittest.TestCase):

    def test_1(self):

        self.assertEqual(random_list, random_list_copy)


if __name__ == '__main__':
    unittest.main()