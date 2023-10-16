def ff(s):
    t = [i.partition('-') for i in s]
    lst = [x for j in range(len(t)) for x in range(int(t[j][0]), int(t[j][2])+1)]
    return lst
a = '1-2,4-4,13-15'.split(',')
print(ff(a))