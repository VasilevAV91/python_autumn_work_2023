import re
s = '+7(812)921-1185, +7(812)145-78-96, +7(921)653-4848, +7(921)101-15-15, +7(812)14-111-15, +7(921)2222-2-22'
def numb(s):
    regex = r'\+7\(812\)\d{3}-\d{4}|\+7\(812\)\d{3}-\d{2}-\d{2}|\+7\(921\)\d{3}-\d{4}|\+7\(921\)\d{3}-\d{2}-\d{2}'
    return re.findall(regex,s)
print(*numb(s),sep=', ')