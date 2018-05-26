from random import random
import colorama
colorama.init(strip=False)
def max_in_list(lst):
    assert lst
    m = lst[0]
    for i in lst:
        if i > m:
            m = i
    return m

M = 5
N = 5
a = []
print('Исходная матрица:')
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print()
print()
print('Итоговая матрица:')
for i in range(N):
    for j in range(M):
        b.append(b[j] / max_in_list(b))
        print("%3d" % b[j], end='')
    a.append(b)
    print()
#print('{color}   | {sum}{endcolor}'.format(color = colorama.Fore.RED,sum = sum(b), endcolor = colorama.Fore.WHITE))