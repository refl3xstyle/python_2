import math as m

a = int(input('Введите основание A: '))
b = int(input('Введите основание B: '))
q = float(input('Введите угол Q: '))

h = (( a - b ) / 2) * m.tan(q) 
result = ((a+b)*h) / 2 

print('Ответ: {}'.format(m.ceil(result)))