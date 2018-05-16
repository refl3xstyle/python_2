import math as m

x = 0.9
t = 2

b = m.log10(m.fabs(x))**2
a = t * x + m.fabs(m.sqrt(b))
result = m.pow((m.cos(a+m.pow(b, 3))), 3)


print('Ответ: {}'.format(m.ceil(result)))