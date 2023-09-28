#Напечатайте ряд чисел Фибоначи до введенного номера n.
n = int(input())
a = [0] * n
a[0] = 1
a[1] = 1
for i in range(2, n):
    a[i] = a[i-1] + a[i-2]
print(*a)