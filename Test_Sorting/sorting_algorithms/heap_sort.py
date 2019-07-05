def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def left_child(a):
    return 2 * a + 1

def parent(a):
    return (a - 1)//2

def sift_down(a, start, end):

    root = start
    to_swap = root

    while left_child(root) <= end:

        child = left_child(root)

        if a[root] < a[child]:
            to_swap = child

        if child + 1 <= end and a[to_swap] < a[child + 1]:
            to_swap = child + 1

        if to_swap == root:
            break

        swap(a, root, to_swap)
        root = to_swap

def heapify(a):

    end = len(a) - 1
    start = parent(end)

    while start >= 0:

        sift_down(a, start, end)
        start -= 1

def maintain_heap(a, end):

    swap(a, 0, end)
    sift_down(a, 0, end - 1)


def heap_sort(a):

    heapify(a)

    end = len(a) - 1

    while end > 0:

        maintain_heap(a, end)
        end -= 1



def sort_method(a):
    heap_sort(a)
    return a
