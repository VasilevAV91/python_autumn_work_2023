def func(x):
    res = ''
    for i in x.lower().split():
        res += ''.join(i.capitalize())
    return res
s = 'cameL cAse woRD'
print(func(s))