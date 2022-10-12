import random

c1 = 0
c2 = 0

for i in range(10001):
    a = [0, 1, 0]
    a.pop(random.choice(a))
    if a[0] + a[1] == 1:
        c1 += 1
    else:
        c2 += 1

print('Вероятность победы при смене выбора', c1/100)
print('Вкроятнось победы при настаивании на своём выборе', c2/100)
