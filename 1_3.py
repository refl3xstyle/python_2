import math as m

x = float(input('Введите число X: '))
y = float(input('Введите число Y: '))
a = float(input('Введите число A: '))
b = float(input('Введите число B: '))

result = (m.sqrt((x+b-a)) + m.log10(y)) / (m.atan((b + a)))

print('Ответ {}'.format(m.ceil(result)))