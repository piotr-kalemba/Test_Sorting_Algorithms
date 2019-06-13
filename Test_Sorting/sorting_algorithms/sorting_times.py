from .heap_sort import heap_sort
from .select_sort import select_sort
from .quick_sort import quick_sort
from .merge_sort import merge_sort
from .bubble_sort import bubble_sort

import time


def bubble_sort_time(a):

    start = time.time()
    bubble_sort(a)
    stop = time.time()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds

def select_sort_time(a):
    start = time.time()
    select_sort(a)
    stop = time.time()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds


def merge_sort_time(a):
    start = time.time()
    merge_sort(a)
    stop = time.time()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds


def quick_sort_time(a):
    start = time.time()
    quick_sort(a)
    stop = time.time()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds


def heap_sort_time(a):
    start = time.time()
    heap_sort(a)
    stop = time.time()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds
