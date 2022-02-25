n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
to = 0
for i in range(n):
    if to <= a[i]:
        ans += 1
        to = a[i] + l

print(ans)
