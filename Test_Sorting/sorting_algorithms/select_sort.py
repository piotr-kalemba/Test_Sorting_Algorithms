def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def select_sort(a):

    for i in range(len(a)):
        j = i + a[i:].index(min(a[i:]))
        swap(a, i, j)

