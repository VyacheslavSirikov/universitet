a = int(input())
b = int(input())
for countNumber in range(a,b+1):
    Number = countNumber
    flip = 0
    while Number >0:
        flip = flip * 10 + Number % 10
        Number = Number // 10
        if countNumber == flip:
            print(countNumber)
