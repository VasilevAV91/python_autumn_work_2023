x = int(input('Введите ключ: '))
dct = {1:1,2:2,3:{2:22,3:{1:111,2:222,3:{0:1111,1:2222,2:3333,3:77}},1:11},6:22}
def func(dct,x):
    lst = []
    for i in dct:
        a = dct.get(i,0)
        if i == x:
            lst.append(a)
        if type(a) == dict:
            lst.extend(func(a,x))
    return lst
print(func(dct,x))
