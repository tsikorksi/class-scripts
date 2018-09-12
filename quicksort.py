# Quicksort algorithm -
# Time Complexity :
# 10    -
# 100   -
# 1000  -
# 10000 -

import random
import time


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
    random_list = random.sample((0, 100), count)
    return random_list


def tester(counts):
    for i in range(0, len(counts)):
        random_list = generator(counts[i])
        total = 0
        for _ in range(0, 5):
            start = time.time()
            quick_sort(random_list)
            end = time.time()
            total += (end-start)
        average = total/5
        print("for " + counts[i] + ' items, average time = ' + average)


tester([10, 100, 1000, 10000])
