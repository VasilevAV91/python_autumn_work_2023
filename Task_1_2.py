# Задача: ввести два числа: x и y.
# Напечатать наибольшее из чисел x+y, x-y, x*y, x/y, x//y
#Первый вариант:
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
print('Наибольшее значение:', max(x+y, x-y, x*y, x/y, x//y))
#Второй вариант:
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
s = x + y, x - y, x * y, x / y, x // y
print(*s) #для контроля
if x + y == max(s): print('Наибольшее значение:', x + y)
elif x - y == max(s): print('Наибольшее значение:', x - y)
elif x * y == max(s): print('Наибольшее значение:', x * y)
elif x / y == max(s): print('Наибольшее значение:', x / y)
else: print('Наибольшее значение:', x // y)
#Третий вариант:
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
list1 = [x + y, x - y, x * y, x / y, x // y]
list1.sort()
print(x + y, x - y, x * y, x / y, x // y)  #для контроля
print('Наибольшее значение:', list1[-1])