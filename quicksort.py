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
