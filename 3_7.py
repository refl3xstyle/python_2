import math as m
import numpy as np
import colorama
colorama.init(strip=False)

f = np.arange(0.1, 2.9, 0.2)
j = 0

def funcgeometr(x):
    param = x
    for i in f:
        f[j] = param**2 - m.sin(param)
    return f

x = float(input('Введите x [0;1]: '))

print('Результат функции: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = funcgeometr(x), endcolor = colorama.Fore.WHITE))

