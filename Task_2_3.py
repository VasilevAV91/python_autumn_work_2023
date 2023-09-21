#Задача: введите число n.
#Сосчитайте и напечатайте факториал числа n!
n = int(input('Введите число n:'))
n_factorial = n
if n == 0:
    n_factorial = 1
else:
    for i in range(1, n):
        n_factorial = n_factorial * i
print(n_factorial)