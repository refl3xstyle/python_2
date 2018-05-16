import math

y = int(input('Введите число Y: '))

result = 3 * y**2 + math.sqrt((y+1))

print('Ответ {}'.format(math.ceil(result)))