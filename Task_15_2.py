import re
s = 'A123BC78 L145IU78 R56KMO178 X666XX178 T589JK78'
def numb(s):
    regex = r'\b[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}1?78'
    return re.findall(regex,s)
print(*numb(s))