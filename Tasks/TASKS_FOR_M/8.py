r = int(input())
b = [int(input()) for i in range(r)]
x = []
for i in range(r):
      if b.count(b[i]) == 1:
            x.append(b[i])
print(x)
