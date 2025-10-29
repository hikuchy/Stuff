import math
import time
from bisect import bisect_left

def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))
arr = read_array("sort.txt")
target = int(input("Какое число нужно найти: "))

def FibonacciSearch(lys, val):
    start_time = time.time()
    if len(lys) == 0:
        end_time = time.time()
        time1 = end_time - start_time
        return -1, time1
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, len(lys) - 1)
        if lys[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif lys[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            end_time = time.time()
            time1 = end_time - start_time
            return i, time1
    if fibM_minus_1 and index + 1 < len(lys) and lys[index + 1] == val:
        end_time = time.time()
        time1 = end_time - start_time
        return index + 1, time1
    end_time = time.time()
    time1 = end_time - start_time
    return -1, time1

FibonacciSearch_result,FibonacciSearch_time = FibonacciSearch(arr,target)
print(f"\t///фибоначи:\n Обьект {target} найден на позиции {FibonacciSearch_result} \n Время выполнения: {FibonacciSearch_time:.6f} секунд")
