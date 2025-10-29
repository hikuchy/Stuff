import random
import time
def generate_array(n, filename):
    arr = [random.randint(-1000, 1000) for _ in range(n)]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, arr)))
n = 100000  # Размер массива
gen_filename = "generation.txt"
sort_filename = "sort.txt"
generate_array(n,gen_filename)
