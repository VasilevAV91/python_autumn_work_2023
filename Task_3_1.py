#Вводить в бесконечном цикле зарплаты сотрудников.
# окончание ввода - 0.
#Напечатать среднюю зарплату
lst = []
while True:
    n = int(input('Введите зарплату:'))
    if n == 0: break
    lst.append(n)
print((sum(lst)/len(lst)))