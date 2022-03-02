n = int(input())
a = [int(input()) for _ in range(n)]

a.reverse()

ans = 0
for i in range(n - 1):
    if a[i] <= a[i + 1]:
        ans += a[i + 1] - a[i] + 1
        a[i + 1] = a[i] - 1

print(ans)
