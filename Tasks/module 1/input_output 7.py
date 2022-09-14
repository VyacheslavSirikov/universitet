a = int(input())  # часы1
b = int(input())  # минуты1
c = int(input())  # секунды1
d = int(input())  # часы2
e = int(input())  # минуты2
f = int(input())  # секунды2
print(d * 3600 + e * 60 + f - (a * 3600 + b * 60 + c))
