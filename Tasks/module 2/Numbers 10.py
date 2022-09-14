print('Введите кол-во учеников в 1 классе')
a = int(input())
print('Введите кол-во учеников во 2 классе')
b = int(input())
print('Введите кол-во учеников в 3 классе')
c = int(input())

a1 = a/2
b1 = b/2
c1 = c/2

if a1 % 1 != 0:
    a1 = a1+1
if b1 % 1 != 0:
    b1 = b1+1
if c1 % 1 != 0:
    c1 = c1+1

print('Нужное кол-во парт')
print(int(a1) + int(b1) + int(c1))
