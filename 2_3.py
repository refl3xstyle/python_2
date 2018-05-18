import colorama
colorama.init(strip=False)

x = int(input('Введите X: '))
y = int(input('Введите Y: '))

if (y > x - 1) & (y < x - 2):
    print('Точки {color}принадлежат{endcolor} функции:'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    print('Точки {color}НЕ принадлежат{endcolor} функции'.format(color = colorama.Fore.LIGHTRED_EX, endcolor = colorama.Fore.WHITE))

