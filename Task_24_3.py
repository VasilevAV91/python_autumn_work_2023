def fu(x):
    dct = {'(':0, ')':0}
    res = 1
    for i in x:
        dct[i] += 1
        if dct[')'] > dct['(']:
            res = 0
            break
        else: pass
        print(dct)
    if dct['('] != dct[')']: res = 0
    return bool(res)

s = '((())()()()()((())()))'
print(fu(s))
