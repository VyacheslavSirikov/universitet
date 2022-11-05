list = [s for s in input().split()]

Max = -1000000
Min = 1000000
MaxInd = 0
MinInd = 0

for i in range(0, len(list)):
    if int(list[i]) > int(Max):
        Max = list[i]
        MaxInd = i
    if int(list[i]) < int(Min):
        Min = list[i]
        MinInd = i

list[MaxInd] = Min
list[MinInd] = Max

print(" ".join(list))
