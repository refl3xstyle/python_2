import math as m 
import colorama
colorama.init(strip=False)


x = int(input('Введите X: '))

f = 1 - m.sin(x)

print('Функция равна: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = f, endcolor = colorama.Fore.WHITE))
