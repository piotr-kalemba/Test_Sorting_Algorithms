from .sorting_algorithms.sorting_times import (bubble_sort_time,
                           select_sort_time,
                           merge_sort_time,
                           quick_sort_time,
                           heap_sort_time)
import random

def create_test_sorting_data(list_length, unique):
    '''the function returns a dictonary whose keys are sorting algorithms' names
    and whose corresponding values are timespans the computer needed to sort
    the random list by the sorting algorithm
    '''
    if unique:
        random_list = list(range(list_length))
        random.shuffle(random_list)
        # in this case we create a random list of a given length whose keys are unique
    else:
        random_list = []
        for _ in range(list_length):
            draw = random.randint(0,list_length * 5)
            random_list.append(draw)
        # in this case we create a random list of a given length whose keys may repeat

    random_list_1 = random_list[:]
    random_list_2 = random_list[:]
    random_list_3 = random_list[:]
    random_list_4 = random_list[:]
    random_list_5 = random_list[:]
    # we create five independent copies of the random list so that sorting any one of them will not affect the others

    data = {}

    data['bubble'] = bubble_sort_time(random_list_1)
    data['select'] = select_sort_time(random_list_2)
    data['merge'] = merge_sort_time(random_list_3)
    data['quick'] = quick_sort_time(random_list_4)
    data['heap'] = heap_sort_time(random_list_5)

    return data