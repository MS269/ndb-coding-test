n, k = map(int, input().split())

dp = [[1], [1, 1]]
for i in range(2, n + 1):
    d = [1]
    for j in range(1, i):
        d.append((dp[i - 1][j] + dp[i - 1][j - 1]) % 10007)
    dp.append(d + [1])

print(dp[n][k])
