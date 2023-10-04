def code(string, n):
    itog = ''
    alfavit_up =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_low =  'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in alfavit_up:
            mesto = alfavit_up.find(i)
            if n <=25:
                if mesto + n <= 26:
                    new_mesto = mesto + n
                else:
                    new_mesto = mesto + n - 26
            else:
                if mesto + n <= 26:
                    new_mesto = mesto + n
                else:
                    new_mesto = mesto + n % 26
            if i in alfavit_up:
                itog += alfavit_up[new_mesto]
            else:
                itog += i
        else:
            mesto = alfavit_low.find(i)
            if n <=25:
                if mesto + n <= 26:
                    new_mesto = mesto + n
                else:
                    new_mesto = mesto + (n - 26)
            else:
                if mesto + n <= 26:
                    new_mesto = mesto + n
                else:
                    new_mesto = mesto + n % 26
            if i in alfavit_low:
                itog += alfavit_low[new_mesto]
            else:
                itog += i
    return itog
print(code(input('Введите сообщение: '), int(input('Введите шаг шифровки: '))))