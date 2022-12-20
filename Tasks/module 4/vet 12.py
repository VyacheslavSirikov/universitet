m = int(input())
d = int(input())
if m == 2:
    if d == 28:
        m += 1
        d = 1
    else:
        d += 1
else:
    if m % 2 == 0:
        if d == 30:
            m += 1
            d = 1
        else:
            d += 1
    else:
        if d == 31:
            m += 1
            d = 1
        else:
            d += 1
print(f'{d}-{m}-2022')