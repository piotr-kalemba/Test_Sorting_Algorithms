import unittest
import random

def copy_list(a, temp, start, stop):

    for k in range(start, stop):
        a[k] = temp[k]

def merge_halves(a, temp, start, middle, stop):

    left, right = start, middle

    for k in range(start, stop):
        if left < middle and (right == stop or a[left] < a[right]):
            temp[k] = a[left]
            left += 1
        else:
            temp[k] = a[right]
            right += 1

    copy_list(a, temp, start, stop)

def mergesort(a, temp, start, stop):

    if stop - start > 1:
        middle = (stop + start)//2
        mergesort(a, temp, start, middle)
        mergesort(a, temp, middle, stop)
        merge_halves(a, temp, start, middle, stop)


def merge_sort(a):

    temp = [0] * len(a)
    mergesort(a, temp, 0, len(a))


# below we run a unittest to make sure if merge_sort indeed sorts a random list:

random_list = []

for _ in range(100):

    draw = random.randint(0,1000)
    random_list.append(draw)

random_list_copy = random_list[:]

merge_sort(random_list)

random_list_copy.sort()

class TestMergeSort(unittest.TestCase):

    def test_1(self):

        self.assertEqual(random_list, random_list_copy)


if __name__ == '__main__':
    unittest.main()