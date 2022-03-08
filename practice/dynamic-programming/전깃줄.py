n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j][1] < a[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
