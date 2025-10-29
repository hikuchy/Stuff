#Сортировка выбором
import random
n=10
a=random.sample(range(21),n)
print(n)
print(a)
for i in range(n-1):
    imin=i
    for j in range(i+1,n):
        if a [imin] > a[j]:
            imin=j
    a[i],a[imin] = a[imin], a[i]
print(a)

