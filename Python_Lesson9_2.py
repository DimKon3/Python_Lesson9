import random

a = []
b = []
res = []

count = int(input("Введите сколько чисел будет в массивах: "))
a = [random.randint(1,100) for _ in range(count)]
b = [random.randint(1,100) for _ in range(count)]

# Вариант 1
#for i in a:
#    if i in b:
#        res.append(i)

#Вариант 2
#res = [i for i in a if i in b]

#Вариант 3
res = list(set(a) & set(b))

print(a)
print()
print(b)
print()
print(res)
print()

print(f"Количество одинаковых элементов в списке равно {len(res)}")