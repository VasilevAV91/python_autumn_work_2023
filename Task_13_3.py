def fun(s):
    yield [x for x in s if x % 2]
lst = [111,21,33,4,5,6,7,8,9,10,11,12,13]
print(*list(*fun(sorted(lst, key = lambda y: y))), end='')
