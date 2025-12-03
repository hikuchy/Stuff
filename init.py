#Сортировка пузырьком
#1
import random
a=[random.randint(-100,10000000000) for i in range(10)]
n = len(a)
print("\n", a)
for i in range(n):
    for j in range(n):
        if a[j] > a[i]:
            a[i], a[j] = a[j], a[i]
print("\n", a)
b=[3,333,666,999,-100000,69,1488,1337,228,0,100000000000000000000000000000000000000000000]
n1=len(b)
print("\n",b)
for c in range(n1):
    for d in range(n1):
        if b[d] > b[c]:
            b[c],b[d] = b[d],b[c]
print("\n",b)
