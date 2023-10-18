def ff():
    n = 1
    while True:
        for i in range(n+1):
            if i % 2:
                yield -n
            else:
                yield n
            n += 1
gf = ff()
for i in range(50):
    print(next(gf), end=',')
