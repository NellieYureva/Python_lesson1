# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, 
# то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

n = 2020
a = n%4
b = n%100
if (a == 0):
    if (b != 0):
        print ("YES")
else:
    print ('NO')