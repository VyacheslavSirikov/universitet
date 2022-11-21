import random


def get_birthday(gr, a):
    count = 0
    for i in range(gr):
        sp = []
        for p in range(a):
            sp.append(random.randint(1, 364))
        if len(set(sp)) != a:
            count += 1
    return f"""Парадокс произошел в: {count / (gr / 100)}% \n"""


print(get_birthday(21, 28))
