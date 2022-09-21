a = 1
while a ==1:
    print('Введите два числа')
    b = int(input())
    c = int(input())
    d = c + b
    print('сумма = ', d)
    print('Если хотите продолжить введите 1, если нет 0')
    p = int(input())
    if p == 1:
        a = 1
    else:
        a = 0
