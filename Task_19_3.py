# Вариант без ввода
class Person:
    def __init__(self, sn, n, o):
        self.sn = sn
        self.n = n
        self.o = o
    def __str__(self, ):
        return f"{self.o[::-1]}{self.n[::-1]}{self.sn[::-1]}"
p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
## Вариант с вводом
class Person:
    def __init__(self, sn, n, o):
        self.sn = ''
        self.n = ''
        self.o = ''
    def set_fio(self):
        fio = input('Введите ФИО: ').split()
        self.sn = fio[0]
        self.n = fio[1]
        self.o = fio[2]
    def __str__(self, ):
        return f"{self.o[::-1]}{self.n[::-1]}{self.sn[::-1]}"
p = Person('','','')
p.set_fio()
print(p)

