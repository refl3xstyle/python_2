def check_n(a,b,c,d):
    if (a % 3) or (b % 3) or (c % 3) or (d % 3):
        if (a % 5) or (b % 5) or (c % 3) or (d % 3):
            print('Оба условия выполняются!')
        else:
            print('Выполняется условие {}'.format(i_f_1))
    else:
        print('Условие НЕ выполняется!')

i_f_1 = 'Одно делится на 3'
i_f_2 = 'Второе делится на 5'
print('{one}, {two} тогда истино'.format(one = i_f_1, two = i_f_2))
        

a = int(input('Введите A: ')) 
b = int(input('Введите B: ')) 
c = int(input('Введите C: ')) 
d = int(input('Введите D: '))

check_n(a,b,c,d)