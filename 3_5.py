import colorama
colorama.init(strip=False)

x = int(input('Введите вашу месячную степендию: '))
y = int(input('Введите ваше месячные расходы на проживание: '))

#Прибыль за 10 месяцев
f1 = x * 10
#Расходы за 10 месяцев 
f2 = (y * 10) * 1.3

if (f1 > f2):
    print('{color}Ты нихера мажор, тебе всего хватит, не ссы!{endcolor}'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE))
else:
    f3 = f2 - f1
    print('Ха бомж, в конце года тебе не хватит: {color}{output}{endcolor} рублей, можешь вскрываться!'.format(color = colorama.Fore.GREEN,output = int(f3), endcolor = colorama.Fore.WHITE))
