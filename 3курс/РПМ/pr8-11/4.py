import time

def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))

n = 1000
gen_filename = "generation.txt"
sort_filename = "sort.txt"
array_to_sort = read_array(gen_filename)

def heapify(nums, heap_size, root_index, swaps_count):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        swaps_count[0] += 1
        heapify(nums, heap_size, largest, swaps_count)

def heap_sort(nums):
    arr_copy = nums.copy()
    n = len(arr_copy)
    swaps_count = [0]

    for i in range(n, -1, -1):
        heapify(arr_copy, n, i, swaps_count)

    for i in range(n - 1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
        swaps_count[0] += 1
        heapify(arr_copy, i, 0, swaps_count)

    return arr_copy, swaps_count[0]

def use_heap(nums):
    start_time = time.time()
    sorted_nums, swaps = heap_sort(nums)
    end_time = time.time()
    time1 = end_time - start_time
    return sorted_nums, swaps, time1

array = read_array(gen_filename)
heap_sorted, heap_swaps, heap_time = use_heap(array)

print("СОРТИРОВКА ПИРАМИДАЛЬНАЯ:")
print(f"Время выполнения: {heap_time:.6f} секунд")
print(f"Количество обменов: {heap_swaps}")

with open(sort_filename, 'w', encoding='utf-8') as f:

    f.write("РЕЗУЛЬТАТЫ СОРТИРОВКИ\n")
    f.write("=" * 50 + "\n")
    f.write("ПИРАМИДАЛЬНАЯ СОРТИРОВКА:\n")
    f.write(f"Время выполнения: {heap_time:.6f} секунд\n")
    f.write(f"Количество обменов: {heap_swaps}\n")
    f.write("-" * 50 + "\n")
