n = int(input())
a = [int(input()) for _ in range(n)]

a.sort(reverse=True)

ans = 0
for i in range(n):
    ans += max(0, a[i] - i)

print(ans)
