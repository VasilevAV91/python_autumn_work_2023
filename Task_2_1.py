#Задача: введите число n. Напишите "таблицу умножения" на число n.
n = int(input('Введите число n:'))
lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    print(f"{i}x{n}={i*n}")
