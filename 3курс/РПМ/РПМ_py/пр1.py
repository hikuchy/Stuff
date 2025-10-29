import random
import time
def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и вернуть время выполнения в
    мс."""
    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res

def is_unique_1(data):
    """Вернуть 'True', если все значения 'data' различны.
    Алгоритм 1:
    Пробежимся по списку с первого до последнего элемента и для каждого из
    них проверим, что такого элемента нет в оставшихся справа элементах.
    Сложность: O(N^2).
    """
    for i in range(len(data)): # O(N)
        if data[i] in data[i+1:]: # O(N) - срез + in: O(N) + O(N) = O(N)
            return False # O(1) - в худшем случае не выполнится
    return True # O(1)
def is_unique_2(data):
    """Вернуть 'True', если все значения 'data' различны.
    Алгоритм 2:
    Отсортируем список. Затем, если в нем есть повторяющиеся элементы, они
    будут расположены рядом — т.о. необходимо лишь попарно их сравнить.
    Сложность: O(N Log N).
    """
    copy = list(data) # O(N)
    copy.sort() # O(N Log N) - «быстрая» сортировка
    for i in range(len(data) - 1): # O(N) - N-1, округлим до O(N)
        if copy[i] == copy[i+1]: # O(1) - [i] и ==, оба по O(1)
            return False # O(1) - в худшем случае не выполнится
    return True # O(1)
def is_unique_3(data):
    """Вернуть 'True', если все значения 'data' различны.
    Алгоритм 3:
    Создадим множество из списка, при создании автоматически удалятся
    дубликаты если они есть. Если длина множества == длине списка, то
    дубликатов нет.
    Сложность: O(N).
    """
    aset = set(data) # O(N)
    return len(aset) == len(data) # O(1) - 2 * len (O(1)) + == O(1)
# Проверка
res = [["i", "1 (мс.)", "2 (мс.)", "3 (мс.)"]]
for i in (100, 500, 1000, 5000, 10000, 20000):
# Из 100000 чисел выбираем 'i' случайных
    data = random.sample(range(-100000, 100000), i)
    res.append([i,
        timeit(is_unique_1, data)[0],
        timeit(is_unique_2, data)[0],
        timeit(is_unique_3, data)[0]])
print("{:>10} {:>10} {:>10} {:>10}".format(*res[0]))
for r in res[1:]:
    print("{:>10} {:>10.2f} {:>10.2f} {:>10.2f}".format(*r))