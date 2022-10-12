a = input()

if a.count('f') > 1:
    print(str(a.find('f')) + ' ' + str(a.rfind('f')))
elif a.count('f') == 1:
    print(a.find('f'))
else:
    print(-1)
