import colorama
colorama.init(strip=False)

x = int(input('Введите X: '))
y = int(input('Введите Y: '))

if (x > 0) and (y < 0):
    print('Точки {color}принадлежат{endcolor} IV четверти :-)'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    print('Точки {color}НЕ принадлежат{endcolor} IV четверти :-('.format(color = colorama.Fore.LIGHTRED_EX, endcolor = colorama.Fore.WHITE))