list1 = [s for s in input().split()]
list2 = [s for s in input().split()]
c = 0

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            c += 1

print(c)