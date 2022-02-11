s = int(input())

n = 1
while True:
    if n ** 2 + n > 2 * s:
        print(n - 1)
        break

    n += 1
