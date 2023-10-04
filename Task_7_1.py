lst_num = []
for i in input('Введите два числа через пробел: ').split():
    lst_num.append(int(i))

lst_del = []
for i in lst_num:
    tes = set()
    for j in range(1, i+1):
        if i % j == 0:
            tes.add(j)
    lst_del.append(tes)
del_max = lst_del[0]
for k in lst_del:
    del_max = del_max.intersection(k)
nod = max(list(del_max))
mul_lst_num = 1
for r in lst_num:
    mul_lst_num *= r

print(mul_lst_num // nod)





