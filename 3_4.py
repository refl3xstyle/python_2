import colorama
from array import array
colorama.init(strip=False)

n = int(input('Введите количество учащихся: '))
a = [0 for x in range(n)]


for i in range(0,n):
    a[i] = int(input('Введите рост {} учащиегося: '.format(i+1)))

f = (sum((a[i] for i in range(0, len(a))))) / len(a)
print('Средний рост учащихся: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = f, endcolor = colorama.Fore.WHITE))