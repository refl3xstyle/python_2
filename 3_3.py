import colorama
colorama.init(strip=False)
n = int(input('Введите n: '))
def pr(r, n=2):
    while n <= r:
        if r % n:
            n += 1
        else:
            r //= n
            yield n

print('Простые делители числа: {color}{output}{endcolor}'.format(color = colorama.Fore.GREEN,output = set(pr(n)), endcolor = colorama.Fore.WHITE))