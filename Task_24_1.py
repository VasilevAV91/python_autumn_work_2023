def sotr_high(x):
    while True:
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                break
        else:
            break
    return lst
lst = [333,1,22,22,4,56,6,3,845,124]
print(sotr_high(lst))