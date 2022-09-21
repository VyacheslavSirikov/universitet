import random

a = 1
while a == 1:

    lives = 3
    print('Кол-во жизней = ', lives)

    d = random.randint(0, 10)
    c = random.randint(0, 10)
    r = random.randint(0, 3)
    o = 0
    f = 0

    if r == 0:
        f = ' - '
        o = d - c
    if r == 1:
        f = ' + '
        o = d + c
    if r == 2:
        f = ' * '
        o = d * c
    if r == 3:
        f = ' // '
        o = d // c

    while lives > 0:

        if lives == 3:
            m = 'Решите пример: '
        if lives != 3:
            m = 'Попробуйте еще раз: '

        print(m, d, f, c)
        op = int(input())

        if op == o:
            print('Вы выиграли')
            break
        if op != o:
            lives = lives - 1
            if lives == 0:
                print('Вы проиграли')
                break
            print('Вы ошиблись. Количество жизней = ', lives, )

    print('Если хотите продолжить введите 1, если нет 0')
    p = int(input())
    if p == 1:
        a = 1
    else:
        a = 0
