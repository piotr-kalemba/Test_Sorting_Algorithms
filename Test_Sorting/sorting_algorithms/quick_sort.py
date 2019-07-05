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


def sort_method(a):
    quick_sort(a)
    return a
