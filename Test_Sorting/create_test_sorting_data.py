from .sorting_algorithms.sorting_times import (bubble_sort_time,
                           select_sort_time,
                           merge_sort_time,
                           quick_sort_time,
                           heap_sort_time)
import random
algorithms_dict = {'bubble' : bubble_sort_time, 'select': select_sort_time, 'merge': merge_sort_time, 'quick': quick_sort_time, 'heap': heap_sort_time}


def create_test_sorting_data(list_length, unique):
    '''the function returns a dictonary whose keys are sorting algorithms' names
    and whose corresponding values are timespans the computer needed to sort
    the random list by given sorting algorithm
    '''
    if unique:
        random_list = list(range(list_length))
        random.shuffle(random_list)
        # in this case we create a random list of a given length whose keys are unique
    else:
        keys_list = list(range(list_length * 3))
        random_list = random.choices(keys_list, k=list_length)
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

def create_algorithm_data(algorithm, unique):

    if unique:

        random_list_10 = list(range(10))
        random_list_100 = list(range(100))
        random_list_1000 = list(range(1000))
        random_list_10000 = list(range(10000))

        random.shuffle(random_list_10)
        random.shuffle(random_list_100)
        random.shuffle(random_list_1000)
        random.shuffle(random_list_10000)

    else:

        keys_list_10 = list(range(10 * 3))
        keys_list_100 = list(range(100 * 3))
        keys_list_1000 = list(range(1000 * 3))
        keys_list_10000 = list(range(10000 * 3))

        random_list_10 = random.choices(keys_list_10, k=10)
        random_list_100 = random.choices(keys_list_100, k=100)
        random_list_1000 = random.choices(keys_list_1000, k=1000)
        random_list_10000 = random.choices(keys_list_10000, k=10000)

    data = {}

    data['10'] = (algorithms_dict[algorithm])(random_list_10)
    data['100'] = (algorithms_dict[algorithm])(random_list_100)
    data['1000'] = (algorithms_dict[algorithm])(random_list_1000)
    data['10000'] = (algorithms_dict[algorithm])(random_list_10000)
    data['algorithm'] = algorithm

    return data
