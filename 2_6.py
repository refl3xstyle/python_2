import colorama
colorama.init(strip=False)


x = int(input('Введите четырехзначеное число: '))

a = int(input('Введите произвольное число a, для проверки второго условия: '))

x = list(map(int,str(x)))

if (x[0] * x[1] * x[2] * x[3]) % 3 == 0:
    print('Первое условие: {color}ВЫПОЛНЯЕТСЯ{endcolor}'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    print('Первое условие: {color}НЕ ВЫПОЛНЯЕТСЯ{endcolor}'.format(color = colorama.Fore.LIGHTRED_EX, endcolor = colorama.Fore.WHITE))

if (x[0] * x[1] * x[2] * x[3]) % a == 0:
    print('Второе условие: {color}ВЫПОЛНЯЕТСЯ{endcolor}'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    print('Второе условие: {color}НЕ ВЫПОЛНЯЕТСЯ{endcolor}'.format(color = colorama.Fore.LIGHTRED_EX, endcolor = colorama.Fore.WHITE))


