def to_rom(number):
    dct = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    res = ''
    while number > 0:
        for k,v in dct.items():
            while number >= k:
                res += v
                number -= k
    return res
print(to_rom(int(input('--->'))))