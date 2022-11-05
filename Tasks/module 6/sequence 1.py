a = [int(s) for s in input().split()]
b = []

for i in a:
    if int(i) % 2 != 0:
        b.append(i)

print(b)