n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if ans % 3 == 0 and i == 0:
        ans += 1
    elif ans % 3 == 1 and i == 1:
        ans += 1
    elif ans % 3 == 2 and i == 2:
        ans += 1

print(ans)
