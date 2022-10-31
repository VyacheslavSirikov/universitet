n = []
a = 1

Max = 1
c = 1

while True:
    a = int(input())
    n.append(a)

    if a == 0:
        break

i = 1

while i < len(n):
    if n[i-1] == n[i]:
        c +=1
        Max = max(Max, c)
    else:
        Max = max(Max, c)
        c = 1

    i += 1

print(Max)


