import math
import time
from bisect import bisect_left

def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))
arr = read_array("sort.txt")
target = int(input("Какое число нужно найти: "))

def LinearSearch(lys, element):
    start_time = time.time()
    for i in range (len(lys)):
        if lys[i] == element:
            end_time = time.time()
            time1 = end_time - start_time
            return i,time1
    end_time = time.time()
    time1 = end_time - start_time
    return -1,time1

def binary_search_recursive(arr, target, left, right):
    start_time = time.time()
    if left > right:
        return -1,0 # Базовый случай: элемент не найден
    mid = (left + right) // 2 # Находим середину массива
    if arr[mid] == target:
        end_time = time.time()
        time1 = end_time - start_time
        return mid,time1 # Базовый случай: элемент найден
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right) #Ищем в правой половине
    else:
        return binary_search_recursive(arr, target, left, mid - 1) #Ищем в левой половине


# # Пример использования:

def JumpSearch(lys, val):
    start_time = time.time()
    length = len(lys)
    if length == 0:
        end_time = time.time()
        time1 = end_time - start_time
        return -1, time1
    jump = int(math.sqrt(length))
    left = 0
    right = 0
    while right < length and lys[right] < val:
        left = right
        right = min(length - 1, right + jump)
    if right >= length and lys[length - 1] < val:
        end_time = time.time()
        time1 = end_time - start_time
        return -1, time1
    for i in range(left, min(right + 1, length)):
        if lys[i] == val:
            end_time = time.time()
            time1 = end_time - start_time
            return i, time1
    end_time = time.time()
    time1 = end_time - start_time
    return -1, time1
#print("0")
Linear_search_res,Linear_search_time = LinearSearch(arr,target)
#print("1")
binary_search_recursive_result,binary_search_recursive_time = binary_search_recursive(arr, target, 0, len(arr) - 1)
#print("2")
JumpSearch_result, JumpSearch_time = JumpSearch(arr,target)

print(f"\t///линейный:\n Обьект {target} найден на позиции {Linear_search_res} \n Время выполнения: {Linear_search_time:.6f} секунд")
print(f"\t///бинарный рекурсивный:\n Обьект {target} найден на позиции {binary_search_recursive_result} \n Время выполнения: {binary_search_recursive_time:.6f} секунд")
print(f"\t///бинарный прыжковый:\n Обьект {target} найден на позиции {JumpSearch_result} \n Время выполнения: {JumpSearch_time:.6f} секунд")
