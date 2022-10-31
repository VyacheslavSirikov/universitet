n = int(input())
a = []
b = 1

while b ** 2 < n:
    c = b ** 2
    a.append(c)
    b += 1

print(a)
