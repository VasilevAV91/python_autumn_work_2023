s = input().split()
lst = ['+', '-', '/', '*']
if s[1] == lst[0]:
    print(int(s[0]) + int(s[2]))
elif s[1] == lst[1]:
    print(int(s[0]) - int(s[2]))
elif s[1] == lst[2]:
    print(int(s[0]) // int(s[2]))
elif s[1] == lst[3]:
    print(int(s[0]) * int(s[2]))
