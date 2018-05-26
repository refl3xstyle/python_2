import math as m
import colorama
colorama.init(strip=False)

def facttop(x,n):
    for i in range(1,n):
        f = x**i+1/m.factorial((i+1)**2)
    return round(f)

x = int(input('Введите количество итераций: '))
y = int(input('Введите x: '))

print('Результат функции: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = facttop(x,y), endcolor = colorama.Fore.WHITE))
