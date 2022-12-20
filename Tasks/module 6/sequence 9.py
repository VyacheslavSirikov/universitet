word = input()

if len(word) % 2 != 0:
    lw = word[:len(word) // 2]
    rw = word[len(word) // 2:]
    lw += word[(len(word) - 1) // 2]
print(rw + lw)