word = list(input('Введите слово: '))
n = int(input('Введите количество слов: '))
k = 1
lst = ['а','у','о','ы','и','э','ю','я','е','ё']
lst1 = []
for i in word:
    if i in lst:
        lst1.append(word.index(i))
lst2 = []
while k <= n:
    lst2.append(list(input('-->')))
    k += 1
lst4 = []
for i in lst2:
    lst3 = []
    for j in i:
        if j in lst:
            lst3.append(i.index(j))
    if lst3 == lst1:
        lst4.append(i)
for r in lst4:
    print(*r)









