a = []
print("Введите последовательность чисел через пробел")
a = list(map(int, input().split()))
print(a)
print()

for i in range(len(a)):
    if a[i] in a[:i:]:
        print("Yes",end=" ")
    else:
        print("No",end=" ")
print()
