import colorama
colorama.init(strip=False)

chr = '_ '
def insert_chr(x):
    if (len(x) <= 25):
        while (len(x) <= 25):
            out = x + chr
            x = out
        return print('Итоговая строка: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = out, endcolor = colorama.Fore.WHITE))
    else: 
        return print('{color}Строка имеет длину больше 25, так что всё 0)00){endcolor}'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))     

x = str(input('Введите произвольную строку: '))
insert_chr(x)