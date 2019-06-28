from .heap_sort import heap_sort
from .select_sort import select_sort
from .quick_sort import quick_sort
from .merge_sort import merge_sort
from .bubble_sort import bubble_sort

import timeit

def bubble_sort_time(a):

    start = timeit.default_timer()
    bubble_sort(a)
    stop = timeit.default_timer()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds

def select_sort_time(a):

    start = timeit.default_timer()
    select_sort(a)
    stop = timeit.default_timer()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds

def quick_sort_time(a):

    start = timeit.default_timer()
    quick_sort(a)
    stop = timeit.default_timer()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds

def merge_sort_time(a):

    start = timeit.default_timer()
    merge_sort(a)
    stop = timeit.default_timer()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds

def heap_sort_time(a):

    start = timeit.default_timer()
    heap_sort(a)
    stop = timeit.default_timer()

    return (stop - start) * 1000
    # sorting time is returned in milliseconds




