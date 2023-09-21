#Задача: введите список lst, состоящий из чисел.
#Найдите и напечатайте наименьшее число из списка lst.
lst = []
for i in range(5):
    a = int(input('Введите число:'))
    lst.append(a)
cur_min = lst[0]
for i in range(len(lst)):
    if lst[i] < cur_min:
        cur_min = lst[i]
print(cur_min)
