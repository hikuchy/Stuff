#Сортировка обменом
a = [2, 5, 4, 6, 7, 1, 10, 11]
n = 7
print(a)
print(n)
for i in range (n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
