max = 0
min =0
a = 1
while a != 0:
    a = int(input())
    if a > max:
        min = max
        max = a
print(min)
