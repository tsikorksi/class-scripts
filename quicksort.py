# Quicksort algorithm - measured with cProfiler
# Time Complexity :
# items | total | sort only
# 1      - 5ms / 0
# 10     - 6ms / 0
# 100    - 7ms / 0
# 1000   - 12ms / 4ms
# 10000  - 120ms / 95ms
# 100000 - 350ms / 199ms (maximum recursion depth reached, algorithm did not finish execution)
# memory usage: since it uses O(logn) memory to store the recursive arrays, this algorithm is quite memory inefficient
# , hence why python stops the process if too many items are present. CPU usage is quite low, as the algorithm is
#  optimised for performance over memory usage

import random


def quick_sort(sorting_array):
    """
    quicksort algorithm
    :param sorting_array: the list to be sorted
    :return: the two split half of the list
    """
    if len(sorting_array) == 1 or len(sorting_array) == 0:
        return sorting_array
    else:
        pivot = sorting_array[0]
        i = 0
        for j in range(len(sorting_array) - 1):
            if sorting_array[j + 1] < pivot:
                sorting_array[j + 1], sorting_array[i + 1] = sorting_array[i + 1], sorting_array[j + 1]
                i += 1
        sorting_array[0], sorting_array[i] = sorting_array[i], sorting_array[0]
        first_part = quick_sort(sorting_array[:i])
        second_part = quick_sort(sorting_array[i + 1:])
        first_part.append(sorting_array[i])
    return first_part + second_part


def generator(count):
    """
    generates lists of random numbers depending on supplied count
    :param count: number of items to generate
    :return: list of random numbers
    """
    random_list = [random.randrange(1, 101, 1) for _ in range(count)]
    return random_list


def tester():
    """
    tests timings of quicksort
    :return:
    """
    count = 10000
    random_list = generator(count)
    quick_sort(random_list)


tester()
