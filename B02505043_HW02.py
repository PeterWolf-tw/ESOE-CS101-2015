tmp = input()

sum = 0
for i in range(len(tmp)):
    sum += 2**i * int(tmp[-(i + 1)])
print(sum)
