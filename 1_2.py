import math as m

n = int(input('Введите число N: '))
y = int(input('Введите число Y: '))

result = (y**2 - 0.8 * y + m.sqrt(y)) / (23.1 * n**2 + m.cos(n))

print('Ответ {}'.format(result))