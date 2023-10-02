# Напишите програму, которая принимает на вход строку из символов и печатает три строки:
# - одну строку из букв,
# - вторую из цифр,
# - третью из прочи символов
# Все строки состоят и уникальных символов
s = input()
a, b, c = set(), set(), set()
for i in s:
    if i in 'abcdefghijklmonpqrstuvwxyz':
        a.add(i)
    elif i in '0123456789':
        b.add(i)
    else:
        c.add(i)
lst = [a,b,c]
for j in lst:
    print(*j)


