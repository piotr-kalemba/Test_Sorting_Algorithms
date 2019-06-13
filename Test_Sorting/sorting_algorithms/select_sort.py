from .bubble_sort import swap

def select_sort(a):

    for i in range(len(a)):
        j = i + a[i:].index(min(a[i:]))
        swap(a, i, j)

