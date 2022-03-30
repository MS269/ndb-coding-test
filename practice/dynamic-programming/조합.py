n, m = map(int, input().split())

dp = [[1] * (i + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][m])
