from collections import Counter

import numpy as np


def parse_file(fd):
    return np.array([list(map(int, r.split())) for r in fd]).T,
  

def task_1(lists):
    pairs = np.sort(lists)
    return sum(abs(pairs[1] - pairs[0]))


def task_2(lists):
    list_1_counted = Counter(lists[0])
    list_2_counted = Counter(lists[1])
    return sum(e1 * c1 * c2 for e1, c1 in list_1_counted.items() if (c2 := list_2_counted.get(e1)))


solution_function_01 = task_1
solution_function_02 = task_2
