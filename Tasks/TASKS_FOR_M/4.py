c = 1
m = 0
p = int(input())
while True:
    a = int(input())
    if a == p:
        c+=1 
    if c > m:
        m = c
    if a != p:
        c = 1
    if (a == 0):
        break
    p = a
print(m)
