
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def bubble_sort(a):

    length = len(a)

    while True:
        swapped = False
        for i in range(1, length):
            if a[i-1] > a[i]:
                swap(a, i-1, i)
                swapped = True
        length -= 1
        if swapped == False or length == 1:
            break



