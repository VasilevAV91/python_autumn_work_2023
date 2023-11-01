import itertools
lst = [50,100,200,500,1000, 5000]
tes = set()
for i in range(1,len(lst)+1):
    for x in itertools.combinations(lst,i):
        tes.add(sum(x))
print(*sorted(tes), sep=', ')