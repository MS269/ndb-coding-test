a, b = map(int, input().split())

ans = 1
while True:
    if a == b:
        break

    if (b % 10 != 1 and b % 2 != 0) or (b < a):
        ans = -1
        break

    if b % 10 == 1:
        b //= 10
        ans += 1
    else:
        b //= 2
        ans += 1

print(ans)
