n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    dp[i][0] += dp[i - 1][0]

    for j in range(1, i):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    dp[i][-1] += dp[i - 1][-1]

print(max(dp[n - 1]))
