num = int(input('Digite um número: '))
f = 1
while num > 0:
    print('{}'.format(num), end='')
    if num > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= num
    num -= 1
print('{}'.format(f))