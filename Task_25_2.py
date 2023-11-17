def is_palindrom(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrom(string[1:-1])
        else:
            return False

s = 'a a, b ,a a'
print(is_palindrom(s))