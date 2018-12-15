liste = [1, 6, 3, 10, 5, 2, 7, 8, 9, 4]

total = 0
for x in liste:
    total = total + x

print(total)

maxValue = liste[0]
for x in liste:
    if x > maxValue:
        maxValue = x

print(maxValue)

fib = [0, 1]
for i in range(0, 8):
    fib.append(fib[-2] + fib[-1])

print(fib)
