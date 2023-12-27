import random

a=[]
count = int(input("Введите сколько чисел будет в массиве: "))
#a = [random.randint(1,200) for _ in range(count)]

for i in range(count):
    a.append(int(input(f"Введите {i+1} число: ")))

print(a)
print()
b=set(a)
print(b)

print(f"Количество различных элементов в списке равно {len(b)}")