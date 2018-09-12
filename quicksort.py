# Quicksort algorithm -
# Time Complexity :
# 1      - 0.005
# 10     - 0.006
# 100    - 0.007
# 1000   - 0.012
# 10000  - 0.120
# 100000 - 0.350 (maximum recursion depth reached, algorithm did not finish execution)

import random


def quick_sort(arr):
    """
    quicksort algorithm
    :param arr:
    :return:
    """
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        i = 0
        for j in range(len(arr) - 1):
            if arr[j + 1] < pivot:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
                i += 1
        arr[0], arr[i] = arr[i], arr[0]
        first_part = quick_sort(arr[:i])
        second_part = quick_sort(arr[i + 1:])
        first_part.append(arr[i])
    return first_part + second_part


def generator(count):
    random_list = [random.randrange(1, 101, 1) for _ in range(count)]
    return random_list


def tester():
    count = 10000
    random_list = generator(count)
    quick_sort(random_list)


tester()
