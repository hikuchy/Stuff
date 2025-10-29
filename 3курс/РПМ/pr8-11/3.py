import math
import time
from bisect import bisect_left

def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))
arr = read_array("sort.txt")
target = int(input("Какое число нужно найти: "))

def ExponentialSearch(lys, val):
    start_time = time.time()
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    res = bisect_left(lys[:min(index, len(lys))],val)
    end_time = time.time()
    time1 = end_time - start_time
    return res,time1

def InterpolationSearch(lys, val):
    start_time = time.time()
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            end_time = time.time()
            time1 = end_time - start_time
            return index,time1
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1,0

ExponentialSearch_result,ExponentialSearch_time = ExponentialSearch(arr,target)

InterpolationSearch_result,InterpolationSearch_time = InterpolationSearch(arr, target)
print(f"\t///экспонициальный:\n Обьект {target} найден на позиции {ExponentialSearch_result} \n Время выполнения: {ExponentialSearch_time:.6f} секунд")
print(f"\t///итерполяционный:\n Обьект {target} найден на позиции {InterpolationSearch_result} \n Время выполнения: {InterpolationSearch_time:.6f} секунд")
