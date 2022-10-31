x = int(input())
y = int(input())

days = 1

while x <= y:
    x += x/10
    days += 1

print(days)
