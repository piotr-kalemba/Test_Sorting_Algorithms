
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def bubble_sort(a):

    length = len(a)

    for i in range(length):
        for j in range(1, length-i):
            if a[j-1] > a[j]:
                swap(a, j-1, j)

