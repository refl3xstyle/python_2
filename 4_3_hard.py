import colorama
colorama.init(strip=False)
# Н и Р буквы
def count_slov(x):
    count_sl = 1
    for i in x:
        if (i == ' '):
            count_sl += 1
    return count_sl

def count_chr_n(x):
    count = 0
    for i in range(0,count_slov(x)):
        if (x[i][0] == 'н') or (x[i][0] == 'Н'):
            count += 1
    return count


x = str(input('Введите произвольную строку: '))

char_list = [count_slov(x)],[len(x)]
test = []

for i in range(0,count_slov(x)):
    char_list[i][0] = x.split(' ')[i]


for i in range(0, count_slov(x)):
    for j in i:
        while (char_list[i][j] != ''):
            char_list[i][j] = x.rindex
    

print(char_list)
#print(x.split(" ")[0])
print('Н: {}'.format(count_chr_n(x)))

#print('Количество слов начинающихся с буквы "н": {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = myString, endcolor = colorama.Fore.WHITE))
#print('Количество слов начинающихся с буквы "р": {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = myString, endcolor = colorama.Fore.WHITE))