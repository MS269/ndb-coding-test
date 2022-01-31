n = int(input())

a = n // 5
b = n % 5

while a >= 0:
    if b % 3 == 0:
        break

    a -= 1
    b += 5

if not a == -1:
    print(a + b // 3)
else:
    print(-1)
