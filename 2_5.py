import colorama
import sys
import math as m
colorama.init(strip=False)

eps = 0.001

x,y = [float(i) for i in input('Введите x, y точки = ').split()]

func = m.sqrt(6 * m.asin(m.pow(x,7) + 4.5 * m.pow(x,6) + 4 * x**2 + 2))

if (abs(func - y) < eps):
    print('Точки {color}лежит{endcolor} на кривой!'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    print('Точки {color}НЕ лежит{endcolor} на кривой!'.format(color = colorama.Fore.LIGHTRED_EX, endcolor = colorama.Fore.WHITE))

