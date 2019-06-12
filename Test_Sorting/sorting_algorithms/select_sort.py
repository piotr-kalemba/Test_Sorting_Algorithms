
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def select_sort(a):

    for i in range(len(a)):

        minimum = min(a[i:])
        j = i + a[i:].index(minimum)
        swap(a, i, j)

