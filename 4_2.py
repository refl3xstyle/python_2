import colorama
colorama.init(strip=False)

chr = '№'
char_list = []
x = str(input('Введите произвольную строку: '))

for i in x:
    char_list.append(i)

for i in range(0,len(char_list)):
    if (chr == char_list[i]):
        char_list[i] = i

myString = ''.join(str(char_list))

print('Итоговая строка: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = myString, endcolor = colorama.Fore.WHITE))