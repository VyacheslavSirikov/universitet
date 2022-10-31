n = []
a = 1
b = 0

while True:
    num = int(input())
    a = num
    n.append(num)

    if a == 0:
        break

i = 0
while i < len(n)-1:
    if n[i] < n[i+1]:
        b += 1
    i += 1

print(b)