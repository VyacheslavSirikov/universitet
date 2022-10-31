n = int(input())
fib_list = [1, 1]

i = 0
while True:
    i += 1
    fib_list.append(fib_list[i-1] + fib_list[i])

    if n == fib_list[i]:
        print(i+1)
        break
    elif n < fib_list[i]:
        print(-1)
        break
