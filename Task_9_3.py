s = list(input().lower())
dct = {}
for i in s:
    dct.setdefault(i, s.count(i))
sorted_dct = sorted(dct.items(), key = lambda x: (-x[1], x[0]))
for j in sorted_dct[0:10]:
    print(f"{j[0]} - {j[1]} ")


