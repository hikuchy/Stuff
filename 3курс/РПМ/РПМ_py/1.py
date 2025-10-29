
import time
def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))

n = 1000
gen_filename = "Generation.txt"
sort_filename = "sort.txt"
array_to_sort = read_array(gen_filename)

def merge(left_list, right_list, swaps_count):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
                swaps_count[0] += left_list_length - left_list_index
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums, swaps_count):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid], swaps_count)
    right_list = merge_sort(nums[mid:], swaps_count)

    return merge(left_list, right_list, swaps_count)

def use_merge(nums):
    swaps_count = [0]
    start_time = time.time()
    sorted_nums = merge_sort(nums, swaps_count)
    end_time = time.time()
    time1 = end_time - start_time
    return sorted_nums, swaps_count[0], time1

def CombSort(ls):
    arr_copy = ls.copy()
    n = len(arr_copy)
    step = n
    flag = True
    swaps = 0
    start_time = time.time()

    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.25)
        flag = False
        i = 0
        while i + step < n:
            if arr_copy[i] > arr_copy[i + step]:
                arr_copy[i], arr_copy[i + step] = arr_copy[i + step], arr_copy[i]
                swaps += 1
                flag = True
            i += 1
    end_time = time.time()
    time1 = end_time - start_time
    return arr_copy, swaps, time1

array = read_array(gen_filename)
merge_sorted, merge_swaps, merge_time = use_merge(array)
Comb_sorted, Comb_swaps, Comb_time = CombSort(array)

print("СОРТИРОВКА РАСЧЁСКОЙ:")
print(f"Время выполнения: {Comb_time:.6f} секунд")
print(f"Количество обменов: {Comb_swaps}")
print("-" * 50)
print("СОРТИРОВКА СЛИЯНИЕМ:")
print(f"Время выполнения: {merge_time:.6f} секунд")
print(f"Количество обменов: {merge_swaps}")
print("-" * 50)
print("СРАВНЕНИЕ АЛГОРИТМОВ:")
print(f"Сортировка слиянием: {merge_time:.6f} сек, обменов: {merge_swaps}")
print(f"Сортировка расчёской: {Comb_time:.6f} сек, обменов: {Comb_swaps}")

with open(sort_filename, 'w', encoding='utf-8') as f:

    f.write("РЕЗУЛЬТАТЫ СОРТИРОВКИ\n")
    f.write("=" * 50 + "\n")
    f.write("СОРТИРОВКА РАСЧЁСКОЙ:\n")
    f.write(f"Время выполнения: {Comb_time:.6f} секунд\n")
    f.write(f"Количество обменов: {Comb_swaps}\n")
    f.write("-" * 50 + "\n")
    f.write("СОРТИРОВКА СЛИЯНИЕМ:\n")
    f.write(f"Время выполнения: {merge_time:.6f} секунд\n")
    f.write(f"Количество обменов: {merge_swaps}\n")
    f.write("-" * 50 + "\n")
    f.write("СРАВНЕНИЕ АЛГОРИТМОВ:\n")
    f.write(f"Сортировка расчёской: {Comb_time:.6f} сек, обменов: {Comb_swaps}\n")
    f.write(f"Сортировка слиянием: {merge_time:.6f} сек, обменов: {merge_swaps}\n")
