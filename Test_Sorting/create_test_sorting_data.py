from .sorting_algorithms.sorting_times import (bubble_sort_time,
                           select_sort_time,
                           merge_sort_time,
                           quick_sort_time,
                           heap_sort_time)
import random

def create_test_sorting_data(list_length, unique):

    if unique:
        random_list = list(range(list_length))
        random.shuffle(random_list)
    else:
        random_list = []
        for _ in range(list_length):
            draw = random.randint(0,list_length * 5)
            random_list.append(draw)

    random_list_1 = random_list[:]
    random_list_2 = random_list[:]
    random_list_3 = random_list[:]
    random_list_4 = random_list[:]
    random_list_5 = random_list[:]

    data = {}

    data['bubble'] = bubble_sort_time(random_list_1)
    data['select'] = select_sort_time(random_list_2)
    data['merge'] = merge_sort_time(random_list_3)
    data['quick'] = quick_sort_time(random_list_4)
    data['heap'] = heap_sort_time(random_list_5)

    return data