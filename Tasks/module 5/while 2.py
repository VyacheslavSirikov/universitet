n = int(input())
t = 1

while 2 ** t <= n:
    t += 1

print(t-1, 2 ** (t-1))
