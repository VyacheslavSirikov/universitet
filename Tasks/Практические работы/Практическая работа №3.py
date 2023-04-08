import random

words = ['олень', 'белый', 'вольт']
f = 2
a = 1
while a == 1:

    ws = '\u25A0\u25A0\u25A0\u25A0\u25A0'
    ws_s = ['\u25A0', '\u25A0', '\u25A0', '\u25A0', '\u25A0', ]

    wn = (random.randint(0, f))
    word = words[wn]

    words.remove(word)

    letters = []
    for i in word:
        letters += i

    lives = 5

    while lives != 0:
        print('количество жизней =', lives)
        print(ws_s)

        print('назовите букву или слово целиком')
        g_word = input()
        g_letter = g_word

        count_letters = 0

        g_v = []
        for i in g_word:
            g_v += i
            count_letters += 1

        if count_letters == 1:
            g_letter = g_word
            g_word = 0
        else:
            g_word = g_word

        if count_letters != 1:
            if g_word == word:
                f -= 1
                if f == -1:
                    print('вы победили! слова закончились')
                    a = 0
                else:
                    print('вы победили!')
                    print('загаданное слово было:', word)
                    print('если хотите начать заново, введите 1, если нет, введите 0')
                    a = int(input())
                break
            else:
                print('вы не угадали!')
                if count_letters == 1:
                    if word.find(g_letter) != -1:
                        for i in range(len(ws_s)):
                            if letters[i] == g_letter:
                                ws_s[i] = letters[i]
                            else:
                                if ws_s[i] == '\u25A0':
                                    ws_s[i] = ws[i]
                lives -= 1


            else:
                print('вы не угадали!')
                lives -= 1

        if ws_s == letters:
            print(ws_s)
            print('вы победили!')
            print('загаданное слово было:', word)
            print('если хотите начать заново, введите 1, если нет, введите 0')
            f -= 1
            if f == -1:
                print('вы победили!')
                a = 0
            else:
                a = int(input())
            break

        if lives == 0:
            print('если хотите начать заново, введите 1, если нет, введите 0')
            f -= 1
            if f == -1:
                print('вы проиграли!')
                a = 0
            else:
                a = int(input())
            break
