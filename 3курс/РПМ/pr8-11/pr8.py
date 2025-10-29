import time

def read_array(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        return list(map(int, data.split()))

n = 1000
gen_filename = "Generation.txt"
sort_filename = "sort.txt"
array_to_sort = read_array(gen_filename)

def insertion_sort(arr):
    arr_copy = arr.copy()
    swaps = 0
    start_time = time.time()
    for i in range(len(arr_copy)):
        cursor = arr_copy[i]
        pos = i
        while pos > 0 and arr_copy[pos - 1] > cursor:
            arr_copy[pos] = arr_copy[pos - 1]
            swaps += 1
            pos = pos - 1
        arr_copy[pos] = cursor
        if pos != i:
            swaps += 1
    end_time = time.time()
    time1 = end_time - start_time
    return arr_copy, swaps, time1

def selection_sort(alist):
    arr_copy = alist.copy()
    swaps = 0
    start_time = time.time()
    for i in range(0, len(arr_copy) - 1):
        smallest = i
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[j] < arr_copy[smallest]:
                smallest = j
        if smallest != i:
            arr_copy[i], arr_copy[smallest] = arr_copy[smallest], arr_copy[i]
            swaps += 1
    end_time = time.time()
    time1 = end_time - start_time
    return arr_copy, swaps, time1

array = read_array(gen_filename)
ins_sorted, ins_swaps, ins_time = insertion_sort(array)
sel_sorted, sel_swaps, sel_time = selection_sort(array)

print("СОРТИРОВКА ВСТАВКАМИ:")
print(f"Время выполнения: {ins_time:.6f} секунд")
print(f"Количество обменов: {ins_swaps}")
print("-" * 50)
print("СОРТИРОВКА ВЫБОРОМ:")
print(f"Время выполнения: {sel_time:.6f} секунд")
print(f"Количество обменов: {sel_swaps}")
print("-" * 50)
print("СРАВНЕНИЕ АЛГОРИТМОВ:")
print(f"Сортировка вставками: {ins_time:.6f} сек, обменов: {ins_swaps}")
print(f"Сортировка выбором: {sel_time:.6f} сек, обменов: {sel_swaps}")

with open(sort_filename, 'w', encoding='utf-8') as f:
    f.write("СОРТИРОВКА ВСТАВКАМИ:\n")
    f.write(' '.join(map(str, ins_sorted)) + '\n')
    f.write("СОРТИРОВКА ВЫБОРОМ:\n")
    f.write(' '.join(map(str, sel_sorted)) + '\n')
    f.write("СРАВНЕНИЕ АЛГОРИТМОВ:\n")
    f.write(f"Сортировка вставками: {ins_time:.6f} сек, обменов: {ins_swaps}\n")
    f.write(f"Сортировка выбором: {sel_time:.6f} сек, обменов: {sel_swaps}\n")
