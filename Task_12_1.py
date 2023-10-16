
lst = [1,2,3,4,1,2,3,4,1,4]
def ff(x):
    lst_ind_min = [x for x in range(len(lst)) if lst[x] == min(lst)]
    lst_ind_max = [x for x in range(len(lst)) if lst[x] == max(lst)]
    return lst_ind_min, lst_ind_max
# lst = list(map(int, input('-->').split()))
print(*ff(lst),sep=',')


