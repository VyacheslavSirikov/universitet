n = int(input())

f1 = 1
f2 = 1

i = 0
while i < n - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i += 1

print(f2)