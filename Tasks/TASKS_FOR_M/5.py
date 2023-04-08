s = []
n = int(input())
ind = []
while n != 0:
    s.append(n)
    n = int(input())
c = len(s)
for i in range(1, len(s)-1):
    if s[i - 1] < s[i] > s[i + 1]:
        ind.append(i)
for i in range(1, len(ind)):
    if c > ind[i] - ind[i - 1]:
        c = ind[i] - ind[i - 1]
print(c)
