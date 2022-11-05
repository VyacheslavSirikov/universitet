b = [s for s in input().split()]
c = [s for s in input().split()]
a = []

for i in range(0, len(b)):
    for j in range(0, len(c)):
        if b[i] == c[j]:
            a.append(b[i])

print(a)
