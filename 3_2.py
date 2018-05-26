import math as m 
import colorama
colorama.init(strip=False)

temp1 = 0
temp2 = 0

k = int(input('Введите k: '))

for i in range(-3,k):
    n1 = ((-1)**i/(i-5)**2)
    temp1 = temp1 + n1
    for n in range(i, 2*k):
        n2 = (m.pow(n,3) - 8) / (n + 4)
        temp2 = temp2 + n2

f = temp1 * temp2 

print('Функция равна: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = f, endcolor = colorama.Fore.WHITE))



