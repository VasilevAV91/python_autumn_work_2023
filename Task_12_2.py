# Создайте списковое включение, которое генерирует следующую последовательность:
# 1,2,2,3,3,3,4,4,4,4 и т.д. до 10
lst = [x for x in range(1,11) for i in range(x)]
print(lst)