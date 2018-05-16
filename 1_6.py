import math as m

l = 0.7
m = 2
w_delta = 4

w = w_delta / (m**2 - 1)

result = m.sqrt((2 * w) / l)



print('Ответ: {}'.format(result))