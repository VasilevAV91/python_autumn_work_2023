import calendar, datetime

year = int(input('Введите год :'))
for month in range(1, 13):
    first_day = calendar.monthrange(year, month)[0]
    if first_day < 3:
        a = 3 - first_day
    elif first_day > 3:
        a = 3 + (7 - first_day)
    else:
        a = 0
    thursday3_date = datetime.date(year, month, a + 15)
    print('Дата бесплатного посещения: ', thursday3_date.strftime('%d.%m.%Y'))