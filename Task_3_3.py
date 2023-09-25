lst = input().split()
long_word = lst[0]
for i in lst:
    if len(i) > len(long_word):
        long_word = i
print(long_word)